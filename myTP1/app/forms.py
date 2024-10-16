from django import forms


from .models import Product, ProductFournisseur, ProductItem, ProductAttribute, Fournisseur , Commande , StoreInventory ,Etat


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        

class ProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = '__all__'

class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = '__all__'


#TP_NOTE



class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'


class ProductFournisseurForm(forms.ModelForm):
    class Meta:
        model = ProductFournisseur
        fields = '__all__'

class StoreInventoryForm(forms.ModelForm):
    class Meta:
        model = StoreInventory
        fields = '__all__'
        
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['produit', 'fournisseur', 'quantite_du_produit', 'etat']  # Ajoutez ou retirez des champs selon vos besoins
        
    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super(CommandeForm, self).__init__(*args, **kwargs)
        if is_update:
            # List the fields you want to make read-only
            read_only_fields = ['produit', 'fournisseur']
            for field in read_only_fields:
                self.fields[field].disabled = True
            
class EtatForm(forms.ModelForm):
    class Meta:
        model = Etat
        fields = '__all__'
        
        
        