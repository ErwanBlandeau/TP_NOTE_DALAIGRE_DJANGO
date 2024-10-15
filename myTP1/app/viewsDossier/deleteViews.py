from django.views.generic import * 
from django.shortcuts import redirect
from ..models import Fournisseur, Product, ProductAttribute, ProductItem ,Commande




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