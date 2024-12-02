from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.api.v1.serializers.plan import PlanSerializer
from core.models.plan import Plan


class PlanViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    lookup_field = "slug"
