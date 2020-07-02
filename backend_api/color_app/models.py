from django.db import models

# Create your models here.
class Colors(models.Model):
	name = models.CharField(max_length = 50, unique = True)
	code = models.CharField(max_length = 50, unique = True)
	status = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "colors"
