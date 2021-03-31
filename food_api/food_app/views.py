
from rest_framework.response import Response
from .serializer import FoodSerializer
from .models import Food
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework import status, viewsets


class FoodViewSet(viewsets.ViewSet):
    model = Food
    serializer_class = FoodSerializer

    def list(self, request):
        object_class = self.model.objects.all()
        query_name = self.request.GET.get('name')
        if query_name is not None:
            object_class = object_class.filter(name__contains=query_name)
        serializer = self.serializer_class(object_class, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        try:
            object_class = self.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound(detail=('That Food does not exist.'))
        serializer = self.serializer_class(object_class)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.get(pk=kwargs.get('pk'))
        except self.model.DoesNotExist:
            raise NotFound(detail=('That Food does not exist.'))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(instance=instance, validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        try:
            instance = self.model.objects.get(pk=kwargs.get('pk'))
        except self.model.DoesNotExist:
            raise NotFound(detail=('That Food does not exist.'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.update(instance=instance, validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            object_class = self.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise NotFound(detail=('That Food does not exist.'))
        object_class.delete()
        return Response({
            'detail': 'That Food is already deleted'
        }, status=status.HTTP_200_OK)