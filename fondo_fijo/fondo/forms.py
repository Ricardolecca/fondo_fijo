from django import forms
from .models import Movimiento

class MovimientoForm(forms.ModelForm):

    class Meta:
        model = Movimiento

        fields = [
            'tipo',
            'categoria',
            'descripcion',
            'valor',
            'fecha'
        ]

        widgets = {
            'fecha': forms.DateInput(
                attrs={'type': 'date'}
            ),

            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripción'
                }
            ),

            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Valor'
                }
            ),
        }