from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Source, Income
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from django.contrib import messages
import json
from django.http import JsonResponse
import datetime




# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    incomes = Income.objects.filter(owner=request.user)
    sources = Source.objects.all()
    paginator = Paginator(incomes, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)
    currency = UserPreference.objects.get(user=request.user).currency
    
    context = {
        'incomes': incomes,
        'page_obj': page_obj,
        'currency': currency,
    }
    return render(request, 'incomes/index.html', context)

def add_income(request):
    sources=Source.objects.all()
    context = {
            'sources': sources,
            'values': request.POST
        }
    if request.method=='GET':
        return render(request, 'incomes/add_income.html', context)
    
    if request.method=='POST':
        wo = request.POST['wo']
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/add_income.html', context)
        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'incomes/add_income.html', context)
        
        source = request.POST['source']
        
        date = request.POST['income_date']
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'incomes/add_income.html', context)
        
        Income.objects.create(owner=request.user, wo=wo, amount=amount, date=date,
                                    source=source, description=description)

        messages.success(request, 'Income saved successfully')
        return redirect('incomes')
    
def edit_income(request, id):
    income = Income.objects.get(pk=id)
    sources = Source.objects.all()


    context = {
                'income': income,
                'values': income,
                'sources': sources
            }
    if request.method=='GET':
        return render(request, 'incomes/edit_income.html', context)
    if request.method=='POST':
        wo = request.POST['wo']
        amount = request.POST['amount']
        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'incomes/edit_income.html', context)
        description = request.POST['description']
        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'incomes/edit_income.html', context)
        
        source = request.POST['source']
        
        date = request.POST['income_date']
        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'incomes/edit_income.html', context)
        
        
        income.owner = request.user
        income.wo = wo
        income.amount = amount
        income.date = date
        income.source = source
        income.description = description
        income.save()
        
        messages.success(request, 'Income edited successfully')
        return redirect('incomes')
    else:
        messages.info(request, 'Handling post form')
        return render(request, 'incomes/edit_income.html', context)
    
def delete_income(request, id):
        income = Income.objects.get(pk=id)
        income.delete()
        messages.success(request, 'Income deleted successfully')
        return redirect('incomes')
    
def search_income(request):
    if request.method=='POST':
        search_str = json.loads(request.body).get('searchText')
        incomes = Income.objects.filter(
            amount__istartswith=search_str, owner = request.user) | Income.objects.filter(
            wo__icontains=search_str, owner = request.user) | Income.objects.filter(
            date__istartswith=search_str, owner = request.user) | Income.objects.filter(
            description__icontains=search_str, owner = request.user) | Income.objects.filter(
            source__icontains=search_str, owner = request.user) 
        data = incomes.values()
        return JsonResponse(list(data), safe=False)
    
def income_source_summary(request):
    todays_date = datetime.date.today()
    last_month = todays_date-datetime.timedelta(days=30*1)
    incomes = Income.objects.filter(owner=request.user, date__gte=last_month, date__lte=todays_date)
    finalrep = {}
    
    def get_source(income):
        return income.source
    
    source_list = list(set(map(get_source, incomes)))
    
    def get_income_source_amount(source):
        amount = 0
        filtered_by_source = incomes.filter(source=source)
        
        for item in filtered_by_source:
            amount += item.amount
        
        return amount
    
    for x in incomes:
        for y in source_list:
            finalrep[y] = get_income_source_amount(y)
    return JsonResponse({'income_source_data': finalrep}, safe=False)
    
def incomes_stats_view(request):
    return render(request, 'incomes/incomes_stats.html')    