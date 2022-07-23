from django.urls import path

from expense.views import AddExpenses, Expenses,EditExpenses,DeleteExpenses
# from invoice.views import ItemDetailView, ItemListView,ItemCreateView, ItemDeleteView, ItemUpdateView
app_name  = 'expense'
urlpatterns = [
    path('expense_create/',AddExpenses,name='expense_create'), 
    path('expense_list/',Expenses, name='expense_list'),
    path('edit_expense/<int:pk>/',EditExpenses, name='edit_expense'),
    path('delete_expense/<int:pk>/',DeleteExpenses, name='delete_expense'),

]
