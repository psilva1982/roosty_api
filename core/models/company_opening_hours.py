from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.models.company import Company


class CompanyOpeningHours(BaseModel):
    DAYS_OF_WEEK = [
        (0, _("Sunday")),
        (1, _("Monday")),
        (2, _("Tuesday")),
        (3, _("Wednesday")),
        (4, _("Thursday")),
        (5, _("Friday")),
        (6, _("Saturday")),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name=_("company"))
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK, verbose_name=_("day of week"))
    opens_at = models.TimeField(verbose_name=_("opens at"))
    closes_at = models.TimeField(verbose_name=_("closes at"))

    def clean(self):
        super().clean()

        # Valida se o horário de abertura é posterior ao horário de fechamento
        if self.opens_at >= self.closes_at:
            raise ValidationError(
                _("Opening time (%(opens_at)s) must be earlier than closing time (%(closes_at)s)."),
                params={"opens_at": self.opens_at, "closes_at": self.closes_at},
            )

        # Valida se há sobreposição de horários para o mesmo dia da semana
        overlapping_hours = CompanyOpeningHours.objects.filter(day_of_week=self.day_of_week).filter(
            Q(opens_at__lt=self.closes_at, closes_at__gt=self.opens_at)
        )

        if self.pk:
            overlapping_hours = overlapping_hours.exclude(pk=self.pk)  # Ignorar o próprio registro em atualizações

        if overlapping_hours.exists():
            raise ValidationError(
                _(
                    "The provided time range (%(opens_at)s - %(closes_at)s) overlaps with another range for the same day."  # noqa: E501
                ),
                params={"opens_at": self.opens_at, "closes_at": self.closes_at},
            )

    class Meta:
        verbose_name = _("Company Opening Hour")
        verbose_name_plural = _("Company Opening Hours")
        unique_together = ("company", "day_of_week", "opens_at", "closes_at")
