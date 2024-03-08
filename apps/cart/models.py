from django.db import models
from apps.cakes.models import Cake
from apps.flours.models import Flour



class BaasketCake(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'Продукт {self.cake.title}'
    
    
    def get_subtotal_sum(self):
        return float(self.quantity * self.cake.price)
    


class BaasketFlour(models.Model):
    flour = models.ForeignKey(Flour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def get_subtotal_sum(self):
        return float(self.quantity * self.flour.price)
    
    def __str__(self):
        return f'Продукт {self.flour.title}'
    
