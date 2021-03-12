from django.shortcuts import render,redirect
# from forex_python.converter import CurrencyRates,CurrencyCodes
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateCurrencyOrderForm,CreateKycForm
from .models import CurrencyOrder,kyc
import json
# import djmoney_rates
# from djmoney_rates.utils import convert_money
# from django.utils.encoding import python_2_unicode_compatible
import requests as r


# Create your views here.
def index(request):
    return render(request,'exapp/index.html')


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



def logout(request):
    auth.logout(request)
    return render(request,'exapp/index.html')


def home(request):
    return render(request,'exapp/home.html')



def buy(request):
    form = CreateCurrencyOrderForm()
    if request.method == "POST":
        form = CreateCurrencyOrderForm(request.POST)
        response = requests.get('https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982')
        data = response.json()
        print(data)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('exapp:kyc')
    else:
        form = CreateCurrencyOrderForm()
    return render(request, 'exapp/buy.html', {'form':form})
       



def orders(request):
    orders = CurrencyOrder.objects.all()
    return render(request,'exapp/orders.html',{'orders':orders})




def profile(request):
    record =  User.objects.all()
    return render(request,'exapp/profile.html',{'record': record})




def account(request):
    return render(request,'exapp/acc.html')




def kyc_add(request):

    # doc = CreateKycForm()
    if request.method == 'POST':
        # doc = CreateKycForm(request.POST,request.FILES)
        # if doc.is_valid():
            pancard = request.FILES['pancard']
            aadhar = request.FILES['aadhar']
            # print(request.FILES)
            doc1 = kyc.objects.create(user=request.user,aadhar=aadhar,pancard=pancard)
            # instance = doc.save(commit=False)
            # instance.user = request.user
            # instance.save()
            messages.info(request,"*Document Uploaded  Sucessfully")
            messages.info(request,"*Note : Your documents is being processed by Processed Manager")

            return redirect('exapp:kyc')
    # else:
    #     form = CreateKycForm()

    return render(request,'exapp/kyc.html')
           

    
        
    



def pay(request):
    if request.method == 'POST':
        order_amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_KqegTBbnvoPiap','BzvLi7pjKrx8TGpWz3R6F6nm'))
        payment = client.order.create({'amount':amount,'currency': 'INR', 'payment_capture':'1'})
    return render(request,'exapp/pay.html')


@csrf_exempt
def success(request):
    return render(request,'exapp/success.html')



def transcation(request):
    return render(request,'exapp/transcation.html')


def usd(request):
    if request.method == 'POST':
        currency_to = request.POST['currency_to']
        currency_from = request.POST['currency_from']
        response = r.get('https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982').json()
        currency_from = currency_to.get('value') * r
        print(response)
    return render(request,'exap/usd.html')
    
    
def euro(request):
    return render(request,'exapp/euro.html')

def dirham(request):
    return render(request,'exapp/dirham.html')

def yuan(request):
    return render(request,'exapp/yuan.html')

def pkr(request):
    return render(request,'exapp/pkr.html')



