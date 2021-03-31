from django.contrib import admin
from django.urls import path
from food_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('foods/', views.FoodList.as_view())
]
