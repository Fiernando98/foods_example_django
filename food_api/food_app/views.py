from drf_query_filter import fields
from rest_framework import viewsets

from .models import Food
from .serializer import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    model = Food
    serializer_class = FoodSerializer
    queryset = model.objects.all()

    query_params = [
        fields.Field('name', 'name__icontains'),
    ]
