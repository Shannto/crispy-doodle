from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm,Textarea
from django.forms.widgets import TextInput
from .models import Product,History
from django import forms


class ProductForm(ModelForm):

    date = forms.DateField(widget=forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2','type': 'date'}))
   
    class Meta:
        model = Product
        fields = ['pieces','feet','mm','types']
        widgets = {
                'pieces': forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'feet': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'mm': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'types': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),
                
                 }


class InvoiceForm(forms.Form):
   qty = forms.IntegerField()
   ft = forms.IntegerField()
   bun = forms.IntegerField()
   total = forms.IntegerField()


class ProductForm2(ModelForm):
   
    class Meta:
        model = Product
        fields = ['pieces','feet','mm','types']
        widgets = {
                'pieces': forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'feet': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'mm': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),
                'types': forms.Select(attrs={'class':'form-control mb-2 mr-sm-2'}),

                 }