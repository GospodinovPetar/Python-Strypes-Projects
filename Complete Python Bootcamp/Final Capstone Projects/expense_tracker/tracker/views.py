from django.shortcuts import render, redirect
from .forms import ExpensesForm

def add_expense(request):
    """
    Renders a form for users to add a new expense.
    On POST, validates and saves the expense data into the database.
    """
    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()  # saves the expense entry in the database
            return redirect('expenses_list')  # You may change this to the name of your success view
    else:
        form = ExpensesForm()

    return render(request, 'expenses/add_expense.html', {'form': form})
