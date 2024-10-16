
from .models import ProductAttributeValue
from app.viewsDossier import *
from rest_framework import viewsets
from .models import (
    Product, Fournisseur, ProductFournisseur, StoreInventory, ProductItem,
    ProductAttribute, ProductAttributeValue, Etat, Commande
)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView , DetailView, TemplateView, FormView, View
from django.urls import reverse_lazy


class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = "detail_attribute.html"
    context_object_name = "productattribute"
    
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail attribut"
        context['values']=ProductAttributeValue.objects.filter(product_attribute=self.object).order_by('position')
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail_product.html"
    context_object_name = "product"
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail produit"
        return context


from .serializers import (
    ProductSerializer, FournisseurSerializer, ProductFournisseurSerializer, StoreInventorySerializer,
    ProductItemSerializer, ProductAttributeSerializer, ProductAttributeValueSerializer, EtatSerializer,
    CommandeSerializer
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class ProductFournisseurViewSet(viewsets.ModelViewSet):
    queryset = ProductFournisseur.objects.all()
    serializer_class = ProductFournisseurSerializer

class StoreInventoryViewSet(viewsets.ModelViewSet):
    queryset = StoreInventory.objects.all()
    serializer_class = StoreInventorySerializer

class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer

class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer

class EtatViewSet(viewsets.ModelViewSet):
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer



