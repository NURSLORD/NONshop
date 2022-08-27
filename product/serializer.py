from rest_framework.serializers import ModelSerializer

from product.models import SubCategory


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
