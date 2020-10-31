from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Server
from .renderers import ServerJSONRenderer
from .serializers import ServerInputSerializer, ServerSerializer

from ..core.paginator_default import DefaultResultsSetPagination


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    permission_classes = (AllowAny, )
    renderer_classes = (ServerJSONRenderer, )
    input_class = ServerInputSerializer
    serializer_class = ServerSerializer
    pagination_class = DefaultResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset

        status = self.request.query_params.get('status', None)
        if status is not None:
            queryset = queryset.filter(status=status)

        server_type = self.request.query_params.get('server_type', None)
        if server_type is not None:
            queryset = queryset.filter(server_type=server_type)

        return queryset

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(page, context=serializer_context, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk):
        input_serializer = self.input_class(data={'id': pk})
        input_serializer.is_valid(raise_exception=True)

        serializer_instance = self.queryset.get(id=input_serializer.data['id'])

        serializer_context = {'request': request}
        serializer = self.serializer_class(serializer_instance, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        input_serializer = self.input_class(data={'id': pk})
        input_serializer.is_valid(raise_exception=True)

        serializer_instance = self.queryset.get(id=input_serializer.data['id'])

        serializer_context = {'request': request}
        serializer_data = request.data.get('server', {})
        serializer = self.serializer_class(serializer_instance, context=serializer_context, data=serializer_data, partial=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
