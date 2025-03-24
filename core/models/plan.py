from django_extensions.db.fields import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.utils.slugify import custom_slugify_function


class Plan(BaseModel):
    name = models.CharField(max_length=64, verbose_name=_("name"), unique=True)
    slug = AutoSlugField(populate_from="name", unique=True, slugify_function=custom_slugify_function)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("discount"))
    enable = models.BooleanField(default=False, verbose_name=_("enable"))

    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plans")
