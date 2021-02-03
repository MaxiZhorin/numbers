from .models import Number_word
from django.forms import ModelForm, TextInput, CheckboxInput, NumberInput


class Number_word_form(ModelForm):
    class Meta:
        model = Number_word
        fields = ['number', 'nds', 'nds_sum']
        widgets = {
            'number': NumberInput(attrs={
                'class':'form-control',
                'placeholder': 'Введите сумму',
                'min': 1,
                'max': 999999999
            }),
            'nds': CheckboxInput(attrs={
                'class': 'form-check-input',
                'placeholder': 'Введите НДС'
            }),
            'nds_sum': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите НДС',
                'value': 20,
                'min': 1,
                'max': 80
            }),
        }
