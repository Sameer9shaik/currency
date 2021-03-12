from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Currency(models.Model):
    id              = models.AutoField(primary_key=True)
    name_choices    =  ( 
                        ('INR','Indian Rupee'),
                        ('USD', 'US Dollar'),
                        ('EURO', 'European Euro'),
                        ('DIRAHAM', 'UA Dirham'),
                        ('YAN', 'Chinese Yuan'),
                        ('PAKISTANI RUPEE', 'Pakistani Rupee'),
                        )
    name          = models.CharField(max_length=15, default='-', choices=name_choices)
    value         = models.DecimalField(max_digits=8, decimal_places=5)

    def __str__(self):
        return self.name



class CurrencyOrder(models.Model):
    id                = models.AutoField(primary_key=True)
    from_choices        = (
                        ('USD', 'US Dollar'),
                        ('EURO', 'European Euro'),
                        ('DIRAHAM', 'UA Dirham'),
                        ('YAN', 'Chinese Yuan'),
                        ('PAKISTANI RUPEE', 'Pakistani Rupee'),

                        )
    currency_from          = models.CharField(max_length=15, default='-', choices=from_choices)
    to_choices      = (
                        ('INR', 'Indian Rupee'),
                        )
    currency_to = models.CharField(max_length=3, default='-', choices=to_choices)
    
    forex_amount         = models.DecimalField(max_digits=8,decimal_places=5,null=True)
    inr_amount               = models.DecimalField(max_digits=8, decimal_places=5,null=True)
    time                 = models.DateTimeField(auto_now_add=True)
    user                 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    


class kyc(models.Model):
    pancard             = models.ImageField(upload_to ='images')
    aadhar              = models.ImageField(upload_to ='images')
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)





