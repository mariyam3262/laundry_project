from django.contrib import admin
from django.urls import path

from notifications.views import WhatsappMessageListView,WhatsappMessageView,WhatsappMessageUpdateView,NotificationListView,SendEmail
app_name  = 'notifications'
urlpatterns = [
    path('list/',WhatsappMessageListView,name='what_list'),
    path('view/',WhatsappMessageView,name='what_view'),
    path('update/',WhatsappMessageUpdateView,name='what_update'),
    path('notification/',NotificationListView,name='notification_list'),
    path('<int:pk>/<str:customer_name>/<str:date>/<str:time>/<str:amount>/email/', SendEmail, name='email')

]
