from .models import Expenses
from django import forms
from .models import Income

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['name', 'expense', 'category', 'date']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['source', 'amount', 'date']

