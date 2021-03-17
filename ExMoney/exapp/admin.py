from django.contrib import admin
from exapp.models import *

class CurrencyOrderAdmin(admin.ModelAdmin):
    list_display        = ['id','currency_from','currency_to','date','forex_amount','inr_amount']
    list_display_links  = ['id','currency_from','currency_to','date','forex_amount','inr_amount']


admin.site.register(CurrencyOrder, CurrencyOrderAdmin)



class CurrencyAdmin(admin.ModelAdmin):
    list_display        = ['id','name','value']
    list_display_links  = ['id','name','value']

admin.site.register(Currency,CurrencyAdmin)



class kycOrderAdmin(admin.ModelAdmin):
    list_display        = ['pancard','aadhar','status']
    list_display_links  = ['pancard','aadhar','status']

admin.site.register(kyc,kycOrderAdmin)

