from django.urls import path
from apps.cakes.views import CakeListView, CakeDetailView, cake_add

urlpatterns = [
    path('cakes/',CakeListView.as_view(),name='cake_list'),
    path('cake/<int:pk>',CakeDetailView.as_view(),name='cake_detail'),
    path('basket-cake-add/<int:pk>/', cake_add, name='cake_add')
]
