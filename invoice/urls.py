from django.urls import path
from invoice.views import ItemDetailView, ItemListView,ItemCreateView, ItemDeleteView, ItemUpdateView
app_name  = 'invoice'
urlpatterns = [
    path('create/',ItemCreateView,name='create'), 
    path('list/',ItemListView, name='list'),
    path('<int:pk>/detail/', ItemDetailView, name='detail'),
    path('<int:pk>/update/',ItemUpdateView,name='update'),
    path('<int:pk>/delete/',ItemDeleteView,name='delete'),

]
