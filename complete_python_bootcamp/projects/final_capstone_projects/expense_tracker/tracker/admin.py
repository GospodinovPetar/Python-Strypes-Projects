from django.contrib import admin
from .models import Expenses, Income


# Register your models here.
@admin.register(Expenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ["expense_id", "name", "category", "date", "expense"]
    search_fields = ["name", "category"]
    list_filter = ["category", "expense", "date"]
    ordering = ["expense"]


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["income_id", "source", "amount", "date"]
    search_fields = ["income_id", "source", "amount", "date"]
    list_filter = ["income_id", "source", "amount", "date"]
    ordering = ["amount", "date"]
