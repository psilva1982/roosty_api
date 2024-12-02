from rest_framework import serializers

from core.models.global_category import GlobalCategory


class GlobalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalCategory
        fields = ["id", "name", "slug"]
