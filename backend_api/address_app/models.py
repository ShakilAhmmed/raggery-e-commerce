from django.db import models


# Create your models here.
class Division(models.Model):
	name = models.CharField(unique = True, max_length = 100)
	slug = models.CharField(max_length = 50, unique = True)
	is_coverage_area = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "divisions"


class District(models.Model):
	division = models.ForeignKey(Division, on_delete = models.CASCADE, related_name = "districts")
	name = models.CharField(unique = True, max_length = 100)
	slug = models.CharField(max_length = 50, unique = True)
	is_coverage_area = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "districts"
