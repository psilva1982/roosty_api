from django_extensions.db.fields import AutoSlugField
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.utils.slugify import custom_slugify_function


class GlobalService(BaseModel):
    name = models.CharField(max_length=64, unique=True, verbose_name=_("name"))
    slug = AutoSlugField(populate_from="name", unique=True, slugify_function=custom_slugify_function)

    class Meta:
        verbose_name = _("Global Service")
        verbose_name_plural = _("Global Services")
