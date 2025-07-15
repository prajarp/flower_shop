from .models import Flower, Color, FlowerArrangement
from django import forms

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = '__all__'

        labels = {
            'name': 'Nazwa kwiatu',
            'colors': 'Kolory',
            'price': 'Cena za sztukę',
            'quantity': 'Ilość w magazynie'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'colors': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }

class FlowerArrangementForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': False, 'class': 'form-control'}),
        required=False,
        label='Zdjęcia'
    )

    class Meta:
        model = FlowerArrangement
        fields = ['name', 'description', 'price', 'stock', 'flowers']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'flowers': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'

        label = {
            'name': 'Kolor'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }