from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateCurrencyOrderForm,CreateKycForm
from .models import CurrencyOrder,kyc
import json
import requests


# main index/home page #
def index(request):
    return render(request,'exapp/index.html')

# creating account # 
def register(request):
    if request.method == 'POST':
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        username = request.POST["username"]
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"*WARNING : Username Already in Use")
                return redirect('http://localhost:8000/exapp/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"*WARNING :Email ID Already in Use")
                return redirect('http://localhost:8000/exapp/register/')
            else:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,"*User Registered Sucessfully")
                return redirect("http://localhost:8000/exapp/login/")
        else:
            messages.info(request,"WARNING :Both Password and Confirm password are not matching")
            return render(request, 'exapp/register.html')
    else:
        return render(request,'exapp/register.html')


    return render(request,'exapp/register.html')


        
# login section #
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        pwd = request.POST['pwd']
        
        user = auth.authenticate(username=username, password=pwd)
        if user :
            auth.login(request, user)
            return redirect('http://localhost:8000/exapp/home/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('http://localhost:8000/exapp/login/')
    else:
        return render(request, 'exapp/login.html')


#logout function #
def logout(request):
    auth.logout(request)
    return render(request,'exapp/index.html')



# home section after logged in #
def home(request):
    record =  User.objects.all()
    orders = CurrencyOrder.objects.all()
    return render(request,'exapp/home.html', {'record':record,'orders':orders})


# view profile #

def profile(request):
    return render(request,'exapp/profile.html')


# acconnt information  section #
def account(request):
    record =  User.objects.all()
    return render(request,'exapp/acc.html',{'record':record})

# transcations #

def orders(request):
    orders = CurrencyOrder.objects.all()
    return render(request,'exapp/orders.html',{'orders':orders})



# buying currency part #

def buy(request):

    if request.method == 'POST':
        currency_from = request.POST['currency_from']
        currency_to = request.POST['currency_to']
        forex_amount = request.POST['forex_amount']

        if currency_from == 'USD':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['USD_INR']
            inr_amount = result * float(forex_amount)
            
          

        elif currency_from == 'euro':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['EUR_INR']
            inr_amount = result * float(forex_amount)

        elif currency_from == 'Dirham':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=MAD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['MAD_INR']
            inr_amount = result * float(forex_amount)


        elif currency_from == 'Yuan':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['CNY_INR']
            inr_amount = result * float(forex_amount)
        

        elif currency_from == 'pkr':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=PKR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['PKR_INR']
            inr_amount = result * float(forex_amount)
            

        if inr_amount >= 10000 and  ( inr_amount % 5 ):
            currency = CurrencyOrder.objects.create(user=request.user,currency_from=currency_from,currency_to=currency_to,forex_amount=forex_amount,inr_amount=inr_amount)
            currency.save()
            return render(request,'exapp/kyc.html')
            # return redirect('exapp/kyc.html')
        
        else:
            messages.info(request,'* Warning : INR Amount must be greater than 10,000 INR and multiples of 500 *')
            return render(request,'exapp/buy.html',{'inr_amount':inr_amount,'forex_amount':forex_amount})

        
        
    else:
        return render(request,'exapp/buy.html')




    
# kyc section #

def kyc_add(request):
    if request.method == 'POST':
        pancard = request.FILES['pancard']
        aadhar = request.FILES['aadhar']
        if pancard and aadhar :
            doc1 = kyc.objects.create(user=request.user,aadhar=aadhar,pancard=pancard)
            messages.info(request,"*Document Uploaded  Sucessfully")
            messages.info(request,"*Sit and Relax : will get back after your  documents is being processed by Processed Manager")
            return redirect('exapp:kyc')
        else:
            messages.info(request,"* Both Documents needs to be uploaded *")
            return redirect('exapp:kyc')

        

        return redirect('exapp:kyc')

    return render(request,'exapp/kyc.html')
           

    
        
    

# payment section #

def pay(request):
    if request.method == 'POST':
        order_amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_KqegTBbnvoPiap','BzvLi7pjKrx8TGpWz3R6F6nm'))
        payment = client.order.create({'amount':amount,'currency': 'INR', 'payment_capture':'1'})
    return render(request,'exapp/pay.html')


# sucess page after payment #
@csrf_exempt
def success(request):
    return render(request,'exapp/success.html')



def transcation(request):
    return render(request,'exapp/transcation.html')


def usd(request):

    if request.method == 'POST':
        currency_from = request.POST['currency_from']
        currency_to = request.POST['currency_to']
        forex_amount = request.POST['forex_amount']
       
        if currency_from == 'USD':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            result = data['USD_INR']
            inr_amount = result * float(forex_amount)
            return render(request,'exapp/usd.html',{'inr_amount':inr_amount})

        else:
            return render(request,'exapp/usd.html')
    
    
def euro(request):
    res = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
    data = res.json()
    curr = data['EUR_INR']
    if request.method == 'GET':
        value = request.GET['inr_amount']
    return render(request,'exapp/euro.html')

def dirham(request):
    res = requests.get("https://free.currconv.com/api/v7/convert?q=MAD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
    data = res.json()
    curr = data['MAD_INR']
    if request.method == 'GET':
        value = request.GET['inr_amount']
    return render(request,'exapp/dirham.html')

def yuan(request):
    res = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
    data = res.json()
    curr = data['CNY_INR']
    if request.method == 'GET':
        value = request.GET['inr_amount']
    return render(request,'exapp/yuan.html')

def pkr(request):
    res = requests.get("https://free.currconv.com/api/v7/convert?q=PKR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
    data = res.json()
    curr = data['PKR_INR']
    if request.method == 'GET':
        value = request.GET['inr_amount']
    return render(request,'exapp/pkr.html')



