from django.urls import path
from apps.main.views import MainListView,about_us


urlpatterns = [
    path('',MainListView.as_view(),name='main_list'),
    path('about',about_us,name='about')
]