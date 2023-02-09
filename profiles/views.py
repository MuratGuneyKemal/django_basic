from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post etc.)',
            'Is similar to a normal Djano view',
            'Mapped manually tp URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})