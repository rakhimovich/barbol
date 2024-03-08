from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from apps.cakes.models import Cake
from apps.cart.models import BaasketCake



class CakeListView(ListView):
    model = Cake
    template_name = 'cakes.html'
    context_object_name = 'cakes'
    
    
class CakeDetailView(DetailView):
    model = Cake
    template_name = 'cake_detail.html'
    context_object_name = 'cake'
    
    
    
def cake_add(request, pk):
    cake = Cake.objects.get(id=pk)
    baskets  = BaasketCake.objects.filter(cake=cake)

    if not baskets.exists():
        BaasketCake.objects.create(cake=cake, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    
    
    