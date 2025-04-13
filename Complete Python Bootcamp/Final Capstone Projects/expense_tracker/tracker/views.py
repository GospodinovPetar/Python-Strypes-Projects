from .forms import ExpensesForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Expenses

def add_expense(request):
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the expense to the database
            return redirect('home')  # Redirect to the list view after saving
    else:
        form = ExpensesForm()
    return render(request, 'add_expense.html', {'form': form})


def home(request):
    expense_list = Expenses.objects.all().order_by('name')
    if request.method == "POST":
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpensesForm()

    context = {
        'expenses': expense_list,
        'form': form,
    }
    return render(request, 'home.html', context)


def expenses_list(request):
    expense_entries = Expenses.objects.all().order_by('name')
    return render(request, 'home.html', {'expenses': expense_entries})


def delete_expense(request, expense_id):
    # Fetch the expense or return 404 if not found.
    expense = get_object_or_404(Expenses, pk=expense_id)

    if request.method == 'POST':
        expense.delete()
        # After deletion, redirect to the expenses list view.
        return redirect('home')

    # Optionally, if you want a confirmation page,
    # you can render one here. For now, we simply redirect.
    return render(request, 'home.html', {'expense': expense})

