from rest_framework.response import Response
from rest_framework.views import APIView


class ApiRootView(APIView):
    def get(self, request, format=None):
        data = {
            # endpoint principal para listagem dos demais endpoints
            "message": "api main view",
        }
        return Response(data)
    