from django.contrib import admin

from core.models.company_opening_hours import CompanyOpeningHours


class CompanyOpeningHoursInlineAdmin(admin.StackedInline):
    model = CompanyOpeningHours
    extra = 1
