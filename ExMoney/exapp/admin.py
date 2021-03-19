from django.contrib import admin
from exapp.models import *

class CurrencyOrderAdmin(admin.ModelAdmin):
    list_display        = ['id', 'user', 'currency_from','currency_to','date','forex_amount','inr_amount']
    list_display_links  = ['id', 'user', 'currency_from','currency_to','date','forex_amount','inr_amount']


admin.site.register(CurrencyOrder, CurrencyOrderAdmin)



class CurrencyAdmin(admin.ModelAdmin):
    list_display        = ['id','name','value']
    list_display_links  = ['id','name','value']

admin.site.register(Currency,CurrencyAdmin)



class kycOrderAdmin(admin.ModelAdmin):
    list_display        = ['user', 'pancard','aadhar','status']
    # readonly_fields = ('pancard','aadhar', )
    list_display_links  = ['user', 'pancard','aadhar','status']

admin.site.register(kyc,kycOrderAdmin)

