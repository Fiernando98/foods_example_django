from django.conf.urls import url
from .views import FoodViewSet


foods_list = FoodViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

food_details = FoodViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', foods_list , name='foods_lists '),
    url(r'^(?P<pk>\d+)/$', food_details , name='food_details '),
]