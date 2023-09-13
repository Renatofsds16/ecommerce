from django.contrib import admin
from .models import Product, Variation

class VariacaoInline(admin.TabularInline):
    model = Variation
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    inlines = [
        VariacaoInline
    ]

@admin.register(Variation)
class VariacaoAdmin(admin.ModelAdmin): 
    list_display = ('name',)


