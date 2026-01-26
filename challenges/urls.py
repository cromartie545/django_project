from django.urls     import path
from . import views
urlpatterns = [
    path('',views.monthly_challenge, name='monthly_challnges' )
]