from django.contrib import admin
from .models import Etat, Fournisseur, Product, ProductAttribute, ProductAttributeValue, ProductFournisseur, ProductItem, StoreInventory ,Commande



class ProductItemAdmin(admin.TabularInline):
    model = ProductItem

class ProductFilter(admin.SimpleListFilter):

    title = 'filtre produit'
    parameter_name = 'custom_status'
    def lookups(self, request, model_admin) :
        return (
        ('online', 'En ligne'),
        ('offline', 'Hors ligne'),
        )
    def queryset(self, request, queryset):
        if self.value() == 'online':
            return queryset.filter(status=1)
        if self.value() == 'offline':
            return queryset.filter(status=0)
        

def set_product_online(modeladmin, request, queryset):
 queryset.update(status=1)
set_product_online.short_description = "Mettre en ligne"
def set_product_offline(modeladmin, request, queryset):
 queryset.update(status=0)
set_product_offline.short_description = "Mettre hors ligne"


admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(Fournisseur)
admin.site.register(ProductFournisseur)
admin.site.register(StoreInventory)
admin.site.register(Commande)
admin.site.register(Etat)


# Register your models here.
