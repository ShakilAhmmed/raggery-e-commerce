from rest_framework import serializers

from .models import Category, SubCategory
from menu_app.serializers import MenuSerializer
from category_app.serializers import CategorySerializer


class SubCategorySerializer(serializers.ModelSerializer):
	menu = MenuSerializer(many = False, read_only = True)
	category = CategorySerializer(many = False, read_only = True)
	menu_id = serializers.IntegerField(write_only = True)
	category_id = serializers.IntegerField(write_only = True)

	class Meta:
		model = SubCategory
		fields = "__all__"
	# depth = 1
