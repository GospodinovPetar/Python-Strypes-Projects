"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from tracker import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("add/", views.add_expense, name="add_expense"),
    path("delete_income/<int:income_id>", views.delete_income, name="delete_income"),
    path("add_income/", views.add_income, name="add_income"),
    path("delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
]
