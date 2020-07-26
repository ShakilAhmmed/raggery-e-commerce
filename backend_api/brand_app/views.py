
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST

# Create your views here.
from .models import Brands
from .serializers import BrandSerializer
from backend_api.pagination import PaginationHandlerMixin, BasicPagination

class BrandApi(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	brand_serializer = BrandSerializer
	def get(self,request, pk =None):
		if pk is None:
			instances = Brands.objects.all()
			page = self.paginate_queryset(instances)
			if page is not None:
				serializer = self.get_paginated_response(self.brand_serializer(page, many = True).data)
			else:
				serializer = self.brand_serializer(instance, many = True)
		else:
			instance = get_object_or_404(Brands, pk = pk)
			serializer = self.brand_serializer(instance = instance)
		return Response(serializer.data, status = HTTP_200_OK)

	def post(self,request):
		serializer = self.brand_serializer(data = request.data)
		response = {}
		if serializer.is_valid():
			serializer.save()
			response['data'] = serializer.data
			response['status'] = HTTP_201_CREATED
		else:
			response['errors'] = serializer.errors
			response['status'] = HTTP_400_BAD_REQUEST
		return Response(response, status = response['status'])

	def put(self, request, pk):
		instance = get_object_or_404(Brands, pk =pk)
		response = {}
		if instance:
			serializer = self.brand_serializer(instance = instance, data = request.data)
			if serializer.is_valid():
				serializer.save()
				response['data'] = serializer.data
				response['status'] = HTTP_201_CREATED
			else:
				response['errors'] = serializer.errors
				response['status'] = HTTP_400_BAD_REQUEST
			return Response(response, status = response['status'])	
		else:
			response['error'] = "Data Not Found"
			response['status'] = HTTP_400_BAD_REQUEST

	def patch(self, request, pk):
		instance = get_object_or_404(Brands, pk = pk)
		response = {}
	
		if instance:
			if instance.status:
				instance.status = False
				response['message'] = "Status Changed Into Inactive"
				response['type'] = False
			else:
				instance.status = True
				response['message'] = "Status Changed Into Active"
				response['type'] = True
			instance.save()
			response['status'] = HTTP_202_ACCEPTED
		else:
			response['message'] = "Data Not Found"
			response['status'] = HTTP_400_BAD_REQUEST
			
		return Response(response, status = response['status'])	
		
	def delete(self, request, pk):
		instance = get_object_or_404(Brands, pk = pk)
		response = {}
		if instance:
			instance.delete()
			response['message'] =  "deleted"
			response['status'] = HTTP_202_ACCEPTED
		else:
			response['error'] = "Data Not Found"
			response['status'] = HTTP_400_BAD_REQUEST
			
		return Response(response, status = response['status'])