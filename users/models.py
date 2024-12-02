import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.manager import UserManager


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(_("email"), unique=True)
    name = models.CharField(_("name"), max_length=256, null=True, blank=False)
    picture = models.ImageField(_("picture"), null=True, blank=True)

    force_change_password = models.BooleanField(
        _("force change password"), default=False, help_text=_("Force user to change password in app")
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    @property
    def abbreviation(self):
        if self.name:
            return self.name[:2].upper()
        return self.email[:2].upper()
