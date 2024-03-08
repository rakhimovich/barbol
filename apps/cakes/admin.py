from django.contrib import admin
from apps.cakes.models import Cake


@admin.register(Cake)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']
