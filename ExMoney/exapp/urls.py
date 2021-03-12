from django.contrib import admin
from django.urls import path,include
from exapp.views import *
from django.conf import settings
from django.conf.urls.static import static



app_name = 'exapp'

urlpatterns = [
    path('index/',index, name='index'),
    path('login/', login_view, name='login'),
    path('register/',register, name='register'),
    path('logout/',logout, name='logout'),
    path('kyc/',kyc_add, name='kyc'),
    path('transcations/',transcation,name='transcations'),
    path('profile/',profile, name='profile'),
    path('account/',account, name='account'),
    path('buy/',buy, name='buy'),
    path('home/',home, name='home'),
    path('orders/',orders, name='orders'),
    path('pay/',pay, name='pay'),
    path('success/',success, name='success'),
    path('usd/',usd, name='usd'),
    path('euro/',euro, name='euro'),
    path('dirham/',dirham, name='dirham'),
    path('yuan/',yuan, name='yuan'),
    path('pkr/',pkr, name='pkr'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)