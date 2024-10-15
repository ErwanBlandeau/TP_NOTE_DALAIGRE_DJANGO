from django.http import HttpResponse ,JsonResponse
from django.views.generic import * 
from django.template.loader import render_to_string
from django.shortcuts import redirect, render


from app.forms import FournisseurForm, ProductAttributeForm, ProductForm, ProductItemForm  ,CommandeForm ,EtatForm 
from django.forms import BaseModelForm
from ..models import Fournisseur, Product, ProductAttribute, ProductItem  ,Commande , Etat ,ProductFournisseur



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
    
# class ProduitSelectionView(View):
#     def get(self, request):
#         form = ProduitSelectionForm()
#         return render(request, 'selection_produit.html', {'form': form})

#     def post(self, request):
#         form = ProduitSelectionForm(request.POST)
#         if form.is_valid():
#             produit = form.cleaned_data['produit']
#             # Utilisez l'ID du produit pour la redirection
#             return redirect('commande-create', produit_id=produit.id)
#         return render(request, 'selection_produit.html', {'form': form})


class CommandeCreateView(CreateView):
    model = Commande
    form_class = CommandeForm
    template_name = "new_commande.html"
    
    def get(self, request):
        produit_id = request.GET.get('produit_id')
        if(produit_id != None):
            fournisseur_ids = ProductFournisseur.objects.filter(product_id=produit_id).values_list('fournisseur', flat=True)
            fournisseurs = Fournisseur.objects.filter(id__in=fournisseur_ids)
            fournisseur_list = []
            for fourni in fournisseurs:
                fournisseur_list.append({'id':fourni.id,"name":fourni.name})
            return JsonResponse(fournisseur_list, safe=False)
        else:
            form = CommandeForm()
            return render(request, "new_commande.html", {'form': form})

    def form_valid(self, form):
        print(form)
        form.save()  # Sauvegarder la commande
        return redirect('commande-list') 



    
    
    
class EtatCreateView(CreateView):
    model = Etat
    form_class = EtatForm
    template_name = "new_etat.html"
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return redirect('commande-list')
    
    
    def EtatCreate(request):
        form = EtatForm()
        if request.method == 'POST':
            form = EtatForm(request.POST)
            if form.is_valid():
                etat = form.save()
                return redirect('commande-list')
        else:
            form = EtatForm()
        return render(request, "new_etat.html", {'form': form})
    
    