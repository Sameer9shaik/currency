from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils.safestring import mark_safe


class Currency(models.Model):
    id              = models.AutoField(primary_key=True)
    name_choices    =  ( 
                        ('INR','Indian (Rupee)'),
                        ('USD', 'United States (Dollar)'),
                        ('EURO', 'European (euro)'),
                        ('DIRAHAM', 'United Amirates (Dirham)'),
                        ('YAN', 'Chinese (Yuan)'),
                        ('PAKISTANI RUPEE', 'Pakistani (Rupee)'),
                        )
    name          = models.CharField(max_length=15, default='-', choices=name_choices)
    value         = models.DecimalField(max_digits=8, decimal_places=5)

    def __str__(self):
        return self.name



class CurrencyOrder(models.Model):
    id                = models.AutoField(primary_key=True)
    from_choices        = (
                       ('USD', 'United States (Dollar)'),
                        ('EURO', 'European (euro)'),
                        ('DIRAHAM', 'United Amirates (Dirham)'),
                        ('YAN', 'Chinese (Yuan)'),
                        ('PAKISTANI RUPEE', 'Pakistani (Rupee)'),

                        )
    currency_from          = models.CharField(max_length=15, default='-', choices=from_choices)
    to_choices      = (
                        ('INR', 'Indian (Rupee)'),
                        )
    currency_to = models.CharField(max_length=3, default='-', choices=to_choices)
    
    forex_amount  = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    inr_amount    = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    total_amount  = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    date          = models.DateField(auto_now=True)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    


class kyc(models.Model):
    pancard             = models.ImageField(upload_to ='images')
    aadhar              = models.ImageField(upload_to ='images')
    status              = models.BooleanField(default=False)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    

    





