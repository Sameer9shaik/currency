from django.contrib import admin
from exapp.models import *

class CurrencyOrderAdmin(admin.ModelAdmin):
    list_display        = ['id', 'date','user', 'currency_from','currency_to','forex_rate', 'Commission_amount','forex_amount','inr_amount']
    list_display_links  = ['id', 'date','user', 'currency_from','currency_to','forex_rate', 'Commission_amount','forex_amount','inr_amount']


admin.site.register(CurrencyOrder, CurrencyOrderAdmin)


class CreateOrderAdmin(admin.ModelAdmin):
    list_display        = ['id', 'date','user', 'currency_from','currency_to','forex_rate', 'Commission_amount','forex_amount','inr_amount']
    list_display_links  = ['id', 'date','user', 'currency_from','currency_to','forex_rate', 'Commission_amount','forex_amount','inr_amount']
admin.site.register(CreateOrder,CreateOrderAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display        = ['user','contact_number','age','city','gender','added_on','update_on']
    list_display_links  = ['user','contact_number','age','city','gender','added_on','update_on']

admin.site.register(Profile,ProfileAdmin)





class CurrencyAdmin(admin.ModelAdmin):
    list_display        = ['id','name','value']
    list_display_links  = ['id','name','value']

admin.site.register(Currency,CurrencyAdmin)



class kycOrderAdmin(admin.ModelAdmin):
    list_display        = ['user', 'pancard','aadhar','status']
    # readonly_fields = ('pancard','aadhar', )
    list_display_links  = ['user', 'pancard','aadhar','status']

admin.site.register(kyc,kycOrderAdmin)

