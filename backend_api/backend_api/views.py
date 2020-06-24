from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class Hello(APIView):
	"""
				Test Calling Api From Vue Js
	"""
	def get(self, request):
		"""
			Test Calling Api From Vue Js
		"""
		return Response({'message': "Hello First Api Calling"}, status = HTTP_200_OK)
