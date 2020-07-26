from rest_framework import serializers
from .models import Sizes


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sizes
        fields = "__all__"