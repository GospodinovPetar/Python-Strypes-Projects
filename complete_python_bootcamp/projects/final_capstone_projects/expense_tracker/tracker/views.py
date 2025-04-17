from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, QuerySet
from .forms import ExpensesForm, IncomeForm
from .models import Expenses, Income


def home(request):
    expenses: QuerySet = Expenses.objects.all().order_by("date")
    incomes: QuerySet = Income.objects.all().order_by("date")

    total_income: float = incomes.aggregate(total=Sum("amount"))["total"] or 0
    total_expenses: float = expenses.aggregate(total=Sum("expense"))["total"] or 0
    net_worth: float = total_income - total_expenses

    expense_breakdown: QuerySet = (
        Expenses.objects.values("category")
        .annotate(total=Sum("expense"))
        .order_by("-total")
    )
    top_expenses: QuerySet = Expenses.objects.all().order_by("-expense")[:3]
    savings_rate: float = (net_worth / total_income * 100) if total_income > 0 else 0

    # Process expense form if POST, else create an empty expense form.
    if request.method == "POST" and "expense" in request.POST:
        expense_form = ExpensesForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect("home")
    else:
        expense_form = ExpensesForm()

    # Always create an empty income form for inline income entry.
    income_form = IncomeForm()

    context: dict = {
        "expenses": expenses,
        "incomes": incomes,
        "form": expense_form,
        "income_form": income_form,
        "net_worth": net_worth,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "expense_breakdown": expense_breakdown,
        "savings_rate": savings_rate,
        "top_expenses": top_expenses,
    }
    return render(request, "home.html", context)


def add_expense(request):
    """
    Create a new expense entry.

    On a POST request, validates and saves the expense using ExpensesForm
    and then redirects to the home view. On a GET request, displays an empty form.
    """
    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ExpensesForm()
    return render(request, "home.html", {"form": form})


def expenses_list(request):
    """
    List all expense entries.

    Retrieves all expenses ordered by name and renders them in the home template.
    """
    expenses: QuerySet = Expenses.objects.all().order_by("name")
    return render(request, "home.html", {"expenses": expenses})


def delete_expense(request, expense_id):
    """
    Delete the expense entry specified by expense_id.

    On a POST request, deletes the expense and redirects to the home view.
    """
    expense: Expenses = get_object_or_404(Expenses, pk=expense_id)
    if request.method == "POST":
        expense.delete()
        return redirect("home")
    return render(request, "home.html", {"expense": expense})


def add_income(request):
    """
    Create a new income entry.

    On a POST request, validates and saves the income using IncomeForm,
    and then redirects to the home view. On a GET request, displays an empty form.
    """
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = IncomeForm()
    return render(request, "home.html", {"form": form})


def delete_income(request, income_id):
    """
    Delete the income entry specified by income_id.

    On a POST request, deletes the income and redirects to the home view.
    """
    income: Income = get_object_or_404(Income, pk=income_id)
    if request.method == "POST":
        income.delete()
        return redirect("home")
    return render(request, "home.html", {"income": income})
