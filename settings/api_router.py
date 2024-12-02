from django.conf import settings
from rest_framework import routers

from core.api.v1.views.global_category import GlobalCategoryViewset
from core.api.v1.views.plan import PlanViewset

if settings.DEBUG:
    router_v1 = routers.DefaultRouter()

else:
    router_v1 = routers.SimpleRouter()

router_v1.register("plan", PlanViewset)
router_v1.register("global-category", GlobalCategoryViewset)
