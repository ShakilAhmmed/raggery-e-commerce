from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import MenuSerializer


# Create your views here.
class MenuApi(APIView):

	def get(self, request):
		return Response({'data': 'Hello'}, status = HTTP_200_OK)

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
