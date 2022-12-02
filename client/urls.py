from django.urls import path
from client import views

urlpatterns = [
    path('myspace/user/settings/', views.userSettings, name='user-settings'),
    path('myspace/user/profile/', views.UserProfile.as_view(), name='user-profile'),
    path('myspace/customers/', views.CustomerListView.as_view(), name='customer-list'),
]
