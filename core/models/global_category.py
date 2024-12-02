from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel


class GlobalCategory(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    slug = AutoSlugField(populate_from="name", unique=True, always_update=False)

    class Meta:
        verbose_name = _("Global Category")
        verbose_name_plural = _("Global Categories")
