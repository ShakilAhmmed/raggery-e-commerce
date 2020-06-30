from rest_framework import serializers

from .models import Category
from menu_app.serializers import MenuSerializer


class CategorySerializer(serializers.ModelSerializer):
	menu = MenuSerializer(many = False, read_only = True)
	menu_id = serializers.IntegerField(write_only = True)

	class Meta:
		model = Category
		fields = "__all__"
		# depth = 1
