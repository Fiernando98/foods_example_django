from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FoodSerializer
from .models import Food


class FoodList(APIView):
    def get(self, request):
        food = Food.objects.all()
        queryName = self.request.GET.get('name')
        if(queryName is not None):
            food = food.filter(name__contains=queryName)
            serializer = FoodSerializer(food, many=True)
            return Response(serializer.data)
