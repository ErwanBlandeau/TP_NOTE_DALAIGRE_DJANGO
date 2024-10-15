from django.views.generic import * 
from django.shortcuts import redirect
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem, StoreInventory , Commande
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "produits"
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('product-list')
    


class ProductItemDeleteView(DeleteView):
    model = ProductItem
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(ProductItemDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "item"
        print(context)
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('product-list')
    

class ProductAttributeDeleteView(DeleteView):
    model = ProductAttribute
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "attribut"
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('product-list')
    


class FournisseurDeleteView(DeleteView):
    model = Fournisseur
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(FournisseurDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "fournisseur"
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('fournisseur-list')
    

class ProductFournisseurDeleteView(DeleteView):
    model = ProductFournisseur
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(ProductFournisseurDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "product_fournisseur"
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('each-fournisseur-product-list', product.id)
    


class StoreInventoryDeleteView(DeleteView):
    model = StoreInventory
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(StoreInventoryDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "product_fournisseur"
        return context
    def post(self, request, **kwargs):
        product = self.get_object()
        product.delete()
        return redirect('each-market-inventory-list')
    
@method_decorator(login_required, name="dispatch")
class CommandeDeleteView(DeleteView):
    model = Commande
    template_name = "delete_total.html"
    def get_context_data(self, **kwargs):
        context = super(CommandeDeleteView, self).get_context_data(**kwargs)
        context['titremenu'] = "commande"
        print(context)
        return context
    def post(self, request, **kwargs):
        commande = self.get_object()
        commande.delete()
        return redirect('commande-list')