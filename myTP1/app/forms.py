from django import forms

from .models import Product, ProductItem, ProductAttribute, Fournisseur

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)


class ProductForm(forms.ModelForm):
    fournisseur = forms.ModelMultipleChoiceField(
        queryset=Fournisseur.objects.all().order_by('code'),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

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