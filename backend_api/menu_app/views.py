from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .models import Menu
from .serializers import MenuSerializer
from backend_api.pagination import PaginationHandlerMixin, BasicPagination


# Create your views here.
class MenuApi(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = MenuSerializer

	def get(self, request):
		instance = Menu.objects.all()
		page = self.paginate_queryset(instance)
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page, many = True).data)
		else:
			serializer = self.serializer_class(instance, many = True)
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
