from django.contrib import admin
from apps.flours.models import Flour


@admin.register(Flour)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']
