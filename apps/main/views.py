from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from apps.cakes.models import Cake

from apps.flours.models import Flour

class MainListView(ListView):
    model = Cake
    template_name = 'index.html'
    # context_object_name = 'products'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        
        context['flours'] = Flour.objects.all()
        context['cakes'] = Cake.objects.all()
        
        return context


def about_us(request):
    return render(request, 'about.html', locals())