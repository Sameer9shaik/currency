from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = 'exapp'

urlpatterns = [
    path('index/',index, name='index'),
    path('login/', login_view, name='login'),
    path('register/',register, name='register'),
    path('logout/',logout, name='logout'),

    path('home/',home, name='home'),
    path('profile/',profile, name='profile'),

    path('orders/',orders, name='orders'),
    path('kyc/',kyc_add, name='kyc'),
    path('transcations/',transcation,name='transcations'),
    path('account/',account, name='account'),
    path('buy/',buy, name='buy'),

    path('pay/',pay, name='pay'),
    path('success/',success, name='success'),

    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)