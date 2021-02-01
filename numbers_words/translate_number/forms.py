from .models import Number_word
from django.forms import ModelForm, TextInput, CheckboxInput, NumberInput


class Number_word_form(ModelForm):
    class Meta:
        model = Number_word
        fields = ['number', 'nds']
        widgets = {
            'number': NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Введите сумму'
            }),
            'nds': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Введите НДС'
            }),
        }
