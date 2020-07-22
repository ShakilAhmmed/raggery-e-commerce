from rest_framework import serializers

from .models import Division, District


class DivisionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Division
		fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
	division = DivisionSerializer(many = False, read_only = True)
	division_id = serializers.IntegerField(write_only = True)

	class Meta:
		model = District
		fields = "__all__"
