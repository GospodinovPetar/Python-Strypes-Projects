from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

class expenses(models.Model):
    categories = [
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Utilities', 'Utilities'),
        ('Groceries', 'Groceries'),
        ('Memberships', 'Memberships'),
        ('Debt', 'Debt'),
        ('Emergency Fund', 'Emergency Fund'),
        ('Other', 'Other')
    ]

    name = models.CharField(max_length=100)
    expense = models.IntegerField(validators=[
        MinValueValidator(1, 'Invalid value')
    ])
    category = models.CharField(max_length=50, choices=categories)
