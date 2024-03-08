from django.urls import path
from apps.cart.views import Basket,QuantityChangeLogics,QuantityChangeLogicsFlour

urlpatterns = [
    path('basket/',Basket.as_view(),name='basket'),
    path('minus/<int:pk>/',QuantityChangeLogics.minus_quantity,name='minus'),
    path('plus/<int:pk>/',QuantityChangeLogics.pilus_quantity,name='plus'),
    path('minusf/<int:pk>/',QuantityChangeLogicsFlour.minus_quantity_f,name='minusf'),
    path('plusf/<int:pk>/',QuantityChangeLogicsFlour.pilus_quantity_f,name='plusf'),
]