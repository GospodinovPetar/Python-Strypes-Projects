from django import forms
from .models import expenses

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = expenses
        fields = ['name', 'expense', 'category']
