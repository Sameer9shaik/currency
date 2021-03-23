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
    value         = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name



class CurrencyOrder(models.Model):
    id                          = models.AutoField(primary_key=True)
    from_choices                = (
                                 ('USD', 'United States (Dollar)'),
                                  ('EURO', 'European (euro)'),
                                  ('DIRAHAM', 'United Amirates (Dirham)'),
                                  ('YAN', 'Chinese (Yuan)'),
                                  ('PAKISTANI RUPEE', 'Pakistani (Rupee)'),

                                  )
    currency_from               = models.CharField(max_length=15, default='-', choices=from_choices)
    to_choices                  =(
                                  ('INR', 'Indian (Rupee)'),
                                  )
    currency_to                 = models.CharField(max_length=3, default='-', choices=to_choices)
    forex_amount                = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    inr_amount                  = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    total_amount                = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    forex_rate                  = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    Commission_amount           = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    date                        = models.DateField(auto_now=True)
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)




class CreateOrder(models.Model):
    id                          = models.AutoField(primary_key=True)
    from_choices                = (
                                 ('USD', 'United States (Dollar)'),
                                  ('EURO', 'European (euro)'),
                                  ('DIRAHAM', 'United Amirates (Dirham)'),
                                  ('YAN', 'Chinese (Yuan)'),
                                  ('PAKISTANI RUPEE', 'Pakistani (Rupee)'),

                                  )
    currency_from               = models.CharField(max_length=15, default='-', choices=from_choices)
    to_choices                  =(
                                  ('INR', 'Indian (Rupee)'),
                                  )
    currency_to                 = models.CharField(max_length=3, default='-', choices=to_choices)
    
    forex_amount                = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    inr_amount                  = models.DecimalField(max_digits=15, decimal_places=2,null=True)
    total_amount                = models.DecimalField(max_digits=15,decimal_places=2,null=True)
    forex_rate                  = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    Commission_amount           = models.DecimalField(max_digits=30,decimal_places=2,null=True)
    date                        = models.DateField(auto_now=True)
    user                        = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


    
class Profile(models.Model):

    contact_number = models.IntegerField()
    age = models.CharField(max_length=250,null=True,blank=True)
    city = models.CharField(max_length=250,null=True,blank=True)
    gender = models.CharField(max_length=250,default="Male")
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  str(self.id)



class kyc(models.Model):
    pancard             = models.ImageField(upload_to ='images')
    aadhar              = models.ImageField(upload_to ='images')
    status              = models.BooleanField(default=False)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    

    





