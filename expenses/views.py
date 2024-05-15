from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
import json
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    expenses = Expense.objects.filter(owner=request.user)
    categories = Category.objects.all()
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    
    context = {
        'expenses': expenses,
        'page_obj': page_obj,
    }
    return render(request, 'expenses/index.html', context)


def add_expense(request):
    categories=Category.objects.all()
    context = {
            'categories': categories,
            'values': request.POST
        }
    if request.method=='GET':
        return render(request, 'expenses/add_expense.html', context)


    if request.method=='POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)
        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/add_expense.html', context)
        
        category = request.POST['category']
        
        date = request.POST['expense_date']
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', context)
        
        Expense.objects.create(owner=request.user, amount=amount, date=date,
                                    category=category, description=description)

        messages.success(request, 'Expense saved successfully')
        return redirect('expenses')

def edit_expense(request, id):
    expense = Expense.objects.get(pk=id)
    categories = Category.objects.all()


    context = {
                'expense': expense,
                'values': expense,
                'categories': categories
            }
    if request.method=='GET':
        return render(request, 'expenses/edit_expense.html', context)
    if request.method=='POST':
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/edit_expense.html', context)
        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/edit_expense.html', context)
        
        category = request.POST['category']
        
        date = request.POST['expense_date']
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/edit_expense.html', context)
        
        
        expense.owner = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description
        expense.save()
        
        messages.success(request, 'Expense edited successfully')
        return redirect('expenses')
    else:
        messages.info(request, 'Handling post form')
        return render(request, 'expenses/edit_expense.html', context)
    
def delete_expense(request, id):
        expense = Expense.objects.get(pk=id)
        expense.delete()
        messages.success(request, 'Expense deleted successfully')
        return redirect('expenses')
    
def search_expenses(request):
    if request.method=='POST':
        search_str = json.loads(request.body).get('searchText')
        expenses = Expense.objects.filter(
            amount__istartswith=search_str, owner = request.user) | Expense.objects.filter(
            date__istartswith=search_str, owner = request.user) | Expense.objects.filter(
            description__icontains=search_str, owner = request.user) | Expense.objects.filter(
            category__icontains=search_str, owner = request.user)
        data = expenses.values()
        return JsonResponse(list(data), safe=False)