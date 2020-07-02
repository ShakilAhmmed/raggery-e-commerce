from rest_framework import serializers
from .models import Colors


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Colors
		fields = "__all__"
