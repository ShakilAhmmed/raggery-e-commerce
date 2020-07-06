from django.db import models

# Create your models here.
from category_app.models import Category
from menu_app.models import Menu


class SubCategory(models.Model):
	menu = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name = "sub_category")
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "sub_category")
	name = models.CharField(max_length = 100, unique = True)
	slug = models.CharField(max_length = 100, unique = True)
	status = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "subcategories"
