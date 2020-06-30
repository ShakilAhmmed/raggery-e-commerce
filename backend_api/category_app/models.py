from django.db import models

from menu_app.models import Menu


# Create your models here.
class Category(models.Model):
	menu = models.ForeignKey(Menu, on_delete = models.CASCADE, related_name = "categories")
	name = models.CharField(max_length = 100, unique = True)
	slug = models.CharField(max_length = 50, unique = True)
	status = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = "categories"
