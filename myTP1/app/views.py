
from .models import ProductAttributeValue
from .viewsDossier.createViews import *
from .viewsDossier.deleteViews import *
from .viewsDossier.updateViews import *
from .viewsDossier.connexionView import *
from .viewsDossier.pageSimple import *
from .viewsDossier.listView import *


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail_product.html"
    context_object_name = "product"
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail produit"
        return context


class ProductAttributeDetailView(DetailView):
    model = ProductAttribute
    template_name = "detail_attribute.html"
    context_object_name = "productattribute"
    
    def get_context_data(self, **kwargs):
        context = super(ProductAttributeDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail attribut"
        context['values']=ProductAttributeValue.objects.filter(product_attribute=self.object).order_by('position')
        return context
    
    
class CommandeDetailView(DetailView):
    model = Commande
    template_name = "detail_commande.html"
    context_object_name = "commande"
    
    def get_context_data(self, **kwargs):
        context = super(CommandeDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail commande"
        context['values']=Commande.objects.all()
        return context
    


