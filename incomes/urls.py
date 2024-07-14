from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


 
urlpatterns = [
    path('incomes/', views.index, name='incomes'),
    path('add_income', views.add_income, name='add-income'),
    path('edit-income/<int:id>', views.edit_income, name='edit-income'),
    path('delete-income/<int:id>', views.delete_income, name='delete-income'),
    path('search-income', csrf_exempt(views.search_income), name='search-income'),
    path('incomes/income_source_summary', views.income_source_summary, name='income_source_summary'),
    path('incomes_stats', views.incomes_stats_view, name='incomes_stats'),

]
