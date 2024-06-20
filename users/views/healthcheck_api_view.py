from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckAPIView(APIView):
    """
    Health check API view to check the status of the API.
    """

    def get(self, request):
        """
        GET method to retrieve the status of the API.
        """
        return Response({"status": "Ok"}, status=status.HTTP_200_OK)
