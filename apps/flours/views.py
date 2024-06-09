from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from apps.cart.models import BaasketFlour
from apps.flours.models import Flour


class FlourListView(ListView):
    model = Flour
    template_name = 'flour.html'
    context_object_name = 'flours'
    
    
class FlourDetailView(DetailView):
    model = Flour
    template_name = 'flour_detail.html'
    context_object_name = 'flour'
    
    
def flour_add(request, pk):
    flour = Flour.objects.get(id=pk)
    baskets  = BaasketFlour.objects.filter(flour=flour)

    if not baskets.exists():
        BaasketFlour.objects.create(flour=flour, quantity=1)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
