from django.shortcuts import render,redirect
from expense.models import Expense
from datetime import datetime,timedelta
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Expenses(request):

    expenses = Expense.objects.all()
        
    return render(request, 'expense/expense_list.html',{'expenses': expenses})

@login_required    
def AddExpenses(request):

    if request.method == "POST":
        detail = request.POST
        expense = Expense()
        expense.expense =  detail['expense_type']
        expense.amount =  detail['amount']
        expense.remarks =  detail['remarks']
        expense.date =datetime.now()
        expense.save()
        return redirect('expense:expense_list')
    return render(request, 'expense/expense.html')

@login_required   
def EditExpenses(request,pk):
    if request.method == 'GET':
        # exit()
        expenses = Expense.objects.get(id=pk)
        return render(request, 'expense/expense_update.html',{'expenses': expenses})
    if request.method == "POST":
        expenses = Expense.objects.get(id=pk)
        detail = request.POST
        expenses.expense =  detail['expense_type']
        expenses.amount =  detail['amount']
        expenses.remarks =  detail['remarks']
        expenses.date = expenses.date
        expenses.save()
        return redirect('expense:expense_list')
        
@login_required
def DeleteExpenses(request,pk):
    expenses = Expense.objects.get(id=pk)
    expenses.delete()
    return redirect('expense:expense_list')