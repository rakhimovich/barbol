from django.urls import path
from apps.flours.views import FlourListView, FlourDetailView,flour_add

urlpatterns = [
    path('flour/',FlourListView.as_view(),name='flour_list'),
    path('flour/<int:pk>',FlourDetailView.as_view(),name='flour_detail'),
    path('basket-flour-add/<int:pk>/', flour_add, name='flour_add')
]