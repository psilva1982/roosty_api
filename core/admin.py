from django.contrib import admin

from core.admin_inline import CompanyOpeningHoursInlineAdmin
from core.models.company import Company
from core.models.global_category import GlobalCategory
from core.models.global_service import GlobalService
from core.models.plan import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "discount", "enable"]


@admin.register(GlobalCategory)
class GlobalCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(GlobalService)
class GlobalServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "plan", "owner", "phone", "address_city", "enable"]
    list_filter = ["category", "plan", "enable"]
    search_fields = ["name", "email", "owner__name"]
    list_select_related = ("category", "owner", "plan")

    inlines = [CompanyOpeningHoursInlineAdmin]
