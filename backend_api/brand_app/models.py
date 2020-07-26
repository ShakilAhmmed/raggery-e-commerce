from django.db import models

# Create your models here.
class Brands(models.Model):
	name = models.CharField(max_length = 50, unique = True)
	slug = models.CharField(max_length = 50, unique = True)
	contact_p = models.CharField(max_length = 100, unique = True)
	address = models.TextField()
	status = models.BooleanField(default = 0)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		db_table = "brands"
