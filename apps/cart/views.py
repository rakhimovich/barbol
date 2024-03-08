from typing import Any
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from apps.cart.models import BaasketCake, BaasketFlour


class Basket(ListView):
    model=BaasketCake
    template_name = 'cart.html'
    context_object_name = 'baskets'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context['baasketflour'] = BaasketFlour.objects.all()
        context['baasketcake'] = BaasketCake.objects.all()
        
        return context
    
class QuantityChangeLogics:
    @staticmethod
    def minus_quantity(request, pk):
        item = BaasketCake.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        item.quantity -= 1
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    @staticmethod
    def pilus_quantity(request, pk):
        item = BaasketCake.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    
class QuantityChangeLogicsFlour:
    @staticmethod
    def minus_quantity_f(request, pk):
        item = BaasketFlour.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        item.quantity -= 1
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    @staticmethod
    def pilus_quantity_f(request, pk):
        item = BaasketFlour.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))