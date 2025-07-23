
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('bus-ticket/', views.bus_ticket, name='bus_ticket'),
    
    path('book_seat/', views.book_seat, name='book_seat'),
    path("subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"),
   
]