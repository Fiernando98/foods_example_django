
from rest_framework.response import Response
from .serializer import FoodSerializer
from .models import Food
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from rest_framework import status, viewsets


class FoodViewSet(viewsets.ModelViewSet):
    model = Food
    serializer_class = FoodSerializer
    queryset = model.objects.all()

