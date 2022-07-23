from django.urls import path
from membership.views import (MemebershipCreateView,MembershipListView,MenbershipDetailView, MembershipUpdateView, MembershipDeleteView, CustMbspCreateView, CustMbspListView, CustMbspUpdateView, CustMbspDeleteView, CustMbspDetailView)

app_name  = 'mbsp'
urlpatterns = [
    path('create/', MemebershipCreateView , name='mbsp-create'),
    path('list/', MembershipListView , name = "mbsp-list"),
    path('<int:pk>/detail/', MenbershipDetailView, name="mbsp-detail"),
    path('<int:pk>/update/', MembershipUpdateView, name="mbsp-update"),
    path('<int:pk>/delete/', MembershipDeleteView, name="mbsp-delete"),
    path('cmbsp-create/', CustMbspCreateView, name='cmbsp-create' ),
    path('cmbsp-list/', CustMbspListView, name='cmbsp-list'),
    path('<int:pk>/cmbsp-detail/', CustMbspDetailView, name='cmbsp-detail'),
    path('<int:pk>/cmbsp-delete/', CustMbspDeleteView, name='cmbsp-delete'),
    path('<int:pk>/cmbsp-update/', CustMbspUpdateView, name='cmbsp-update')

]
