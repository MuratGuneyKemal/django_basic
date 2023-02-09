from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


from profiles import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post etc.)',
            'Is similar to a normal Djano view',
            'Mapped manually tp URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create Hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """Handle Partial Update of an Object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method': 'Delete'})
    

class HelloViewSet(viewsets.ViewSet):
    """Viewset test"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """"""

        a_viewset = [
            'Uses list create retrieve update partial_update',
            'Automatically maps o URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """acts like post"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an obj by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle Update of an Object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle Partial Update of an Object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an Object"""
        return Response({'http_method': 'DELETE'})