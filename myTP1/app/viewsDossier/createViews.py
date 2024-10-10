from django.http import HttpResponse
from django.views.generic import * 

from django.shortcuts import redirect, render
from app.forms import ProductAttributeForm, ProductForm, ProductItemForm ,CommandeForm
from django.forms import BaseModelForm
from ..models import Product, ProductAttribute, ProductItem ,Commande


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
    
    