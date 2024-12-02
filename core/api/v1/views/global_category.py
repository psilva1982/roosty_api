from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.api.v1.serializers.global_category import GlobalCategorySerializer
from core.models.global_category import GlobalCategory


class GlobalCategoryViewset(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = GlobalCategory.objects.all()
    serializer_class = GlobalCategorySerializer

    lookup_field = "slug"
