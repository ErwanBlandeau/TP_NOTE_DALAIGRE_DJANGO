from django.http import HttpResponse
from django.views.generic import * 

from django.shortcuts import redirect, render
from app.forms import FournisseurForm, ProductAttributeForm, ProductForm, ProductItemForm
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductFournisseur, ProductItem


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
    

# ----------------- TP NOTEE -----------------

class FournisseurCreateView(CreateView):
    model = Fournisseur
    form_class = FournisseurForm
    template_name = "new_product.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('fournisseur-list')
    
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
    

class ProductFournisseurCreateView(CreateView):
    model = ProductFournisseur
    fields = ['product', 'fournisseur']
    template_name = "new_product.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('fournisseur-list')
    

def ProductFournisseurCreate(request):
    if request.method == 'POST':
        product = ProductFournisseur.objects.get(pk=request.POST.get('product'))
        fournisseurs = request.POST.getlist('fournisseur')
        for fournisseur in fournisseurs:
            ProductFournisseur.objects.create(product=product, fournisseur=Fournisseur.objects.get(pk=fournisseur))
        return redirect('product-detail', product.id)
    return render(request, "new_product.html", {'product': Product.objects.get(pk=request.GET.get('product'))})


