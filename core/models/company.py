from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseModel
from core.models.global_category import GlobalCategory
from core.models.plan import Plan

User = get_user_model()


class Company(BaseModel):
    category = models.ForeignKey(GlobalCategory, on_delete=models.PROTECT, verbose_name=_("category"))
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_("owner"))
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, verbose_name=_("plan"))
    name = models.CharField(max_length=128, verbose_name=_("name"))
    email = models.EmailField(max_length=128, verbose_name=_("email"))
    phone = models.CharField(max_length=32, verbose_name=_("phone"))
    address_street = models.CharField(max_length=254, verbose_name=_("address street"))
    address_number = models.CharField(max_length=20, verbose_name=_("address number"))
    address_neighborhood = models.CharField(max_length=64, verbose_name=_("address neighborhood"))
    address_city = models.CharField(max_length=64, verbose_name=_("address city"))
    address_state = models.CharField(max_length=32, verbose_name=_("address state"))
    enable = models.BooleanField(default=False, verbose_name=_("enable"))
