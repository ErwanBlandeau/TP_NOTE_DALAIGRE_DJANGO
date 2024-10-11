from django.http import HttpResponse
from django.views.generic import * 

from django.shortcuts import redirect, render

from app.forms import FournisseurForm, ProductAttributeForm, ProductForm, ProductFournisseurForm, ProductItemForm  ,CommandeForm, StoreInventoryForm
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem  ,Commande, StoreInventory



class ProductCreateView(CreateView):
    model = Product
    form_class=ProductForm
    template_name = "new_product.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)



def ProductCreate(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product-detail', product.id)
    else:
        form = ProductForm()
    return render(request, "new_product.html", {'form': form})

class FournisseurCreateView(CreateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "new_product.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)
    
def FournisseurCreate(request):
    form = FournisseurForm()
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('fournisseur-list')
    else:
        form = FournisseurForm()
    return render(request, "new_product.html", {'form': form})
    

class ProductAttributeCreateView(CreateView):
    model = ProductAttribute
    form_class=ProductAttributeForm
    template_name = "new_product.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('attribute-list')
    
    

class ProductItemCreateView(CreateView):
    model = ProductItem
    form_class = ProductItemForm
    template_name = "new_product.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('item-list')
    
    
class CommandeCreateView(CreateView):
    model = Commande
    form_class = CommandeForm
    template_name = "new_commande.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('commande-list')
    
    

class ProductFournisseurCreateView(CreateView):
    model = ProductFournisseur
    form_class = ProductFournisseurForm
    template_name = "new_product.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('product-detail', product.id)
    
def ProductFournisseurCreate(request):
    form = ProductFournisseurForm()
    if request.method == 'POST':
        form = ProductFournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('each-fournisseur-product-list')
    else:
        form = ProductFournisseurForm()
    return render(request, "new_product.html", {'form': form})




class StoreInventoryCreateView(CreateView):
    model = StoreInventory
    form_class = StoreInventoryForm
    template_name = "new_product.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        product = form.save()
        return redirect('each-market-inventory-list')
    
def StoreInventoryCreate(request):
    form = StoreInventoryForm()
    if request.method == 'POST':
        form = StoreInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('each-market-inventory-list')
    else:
        form = StoreInventoryForm()
    return render(request, "new_product.html", {'form': form})