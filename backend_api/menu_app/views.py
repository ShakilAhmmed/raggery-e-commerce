from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_202_ACCEPTED, \
	HTTP_204_NO_CONTENT

from .models import Menu
from .serializers import MenuSerializer
from backend_api.pagination import PaginationHandlerMixin, BasicPagination
from django.db.models import Q


# Create your views here.
class MenuApi(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = MenuSerializer

	def get(self, request, pk = None):
		if pk is None:
			instance = Menu.objects.all()
			filter_by = request.GET.get('q', None)
			if filter_by is not None:
				instance = instance.filter(Q(name__icontains = filter_by) | Q(slug__icontains = filter_by))
			page = self.paginate_queryset(instance)
			if page is not None:
				serializer = self.get_paginated_response(self.serializer_class(page, many = True).data)
			else:
				serializer = self.serializer_class(instance, many = True)
			return Response(serializer.data, status = HTTP_200_OK)
		else:
			instance = get_object_or_404(Menu, pk = pk)
			serializer = self.serializer_class(instance = instance)
			return Response(serializer.data, status = HTTP_200_OK)

	def post(self, request):
		serialize = MenuSerializer(data = request.data)
		response = {}
		if serialize.is_valid():
			serialize.save()
			response['data'] = serialize.data
			response['status'] = HTTP_201_CREATED
		else:
			response['errors'] = serialize.errors
			response['status'] = HTTP_400_BAD_REQUEST
		return Response(response, status = response['status'])

	def put(self, request, pk):
		instance = get_object_or_404(Menu, pk = pk)
		serialize = self.serializer_class(instance = instance, data = request.data)
		response = {}
		if serialize.is_valid():
			serialize.save()
			response['data'] = serialize.data
			response['status'] = HTTP_201_CREATED
		else:
			response['errors'] = serialize.errors
			response['status'] = HTTP_400_BAD_REQUEST
		return Response(response, status = response['status'])

	def patch(self, request, pk):
		instance = get_object_or_404(Menu, pk = pk)
		response = {}
		if instance.status:
			instance.status = False
			response['message'] = "Status Changed Into Inactive"
			response['type'] = False
		else:
			instance.status = True
			response['message'] = "Status Changed Into Active"
			response['type'] = True
		instance.save()
		return Response(response, status = HTTP_202_ACCEPTED)

	def delete(self, request, pk):
		instance = get_object_or_404(Menu, pk = pk)
		instance.delete()
		response = {"message": "deleted"}
		return Response(response, status = HTTP_204_NO_CONTENT)

class GetMenu(ListAPIView):
	serializer_class = MenuSerializer
	queryset = Menu.objects.filter(status = 1)

