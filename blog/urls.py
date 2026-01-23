from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('setsession/', views.setsession, name='set-session'),
    path('getsession/', views.getsession, name='get-session'),
    path('delsession/', views.delsession, name='del-session'),
    path('clearsession/', views.clearsession, name='clear-session'),
    path('visitcount/', views.visitcount, name='visit-count'),
    path('setexpiry/', views.setexpiry, name='set-expiry'),
    path('checkexpiry/', views.checkexpiry, name='check-expiry'),
    path('clearsessionexpiry/', views.clearsessionexpiry, name='clear-session-expiry'),
    path('customexpiry/', views.customexpiry, name='custom-expiry'),
    path('checkcustomexpiry/', views.checkcustomexpiry, name='check-custom-expiry'),
    path('deletecustomexpiry/', views.deletecustomexpiry, name='delete-custom-expiry'),
    path('incrementcounter/', views.incrementcounter, name='increment-counter'),
    path('resetcounter/', views.resetcounter, name='reset-counter'),
    path('getcounter/', views.getcounter, name='get-counter'),
    path('deletecounter/', views.deletecounter, name='delete-counter'),
    path('setmultiplekeys/', views.setmultiplekeys, name='set-multiple-keys'),
    path('getmultiplekeys/', views.getmultiplekeys, name='get-multiple-keys'),
    path('deletemultiplekeys/', views.deletemultiplekeys, name='delete-multiple-keys'), 
]    