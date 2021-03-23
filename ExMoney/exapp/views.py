from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateCurrencyOrderForm,CreateKycForm, CreateUserForm
from .models import CurrencyOrder,kyc,Profile,CreateOrder
import json
import requests
import re


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
                messages.info(request," Username Already in Use....!")
                return redirect('exapp:register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email ID Already in Use....!")
                return redirect('exapp:register')

                if username == any(c.islower() for c in username):
                    messages.info(request,"Atleast 1 Lower Character should use.....!")
                if username == any(c.isupper() for c in username):
                    messages.info(request,"Atleast 1 Upper Character should use.....!")
                if username == any(c.isupper() for c in username):
                    messages.info(request,"Atleast 1 Upper Character should use.....!")
                if username == any(c.isdigit() for c in username):
                    messages.info(request,"Atleast 1 Digit  should use.....!")
                if len(username) is not 6:
                    messages.info(request,'Min 6 characters should use ....!')
            else:

                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,"User Registered Sucessfully....!")
                return redirect("exapp:login")
        else:
            messages.info(request,"Both Password and Confirm password are not matching....!")
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
            return redirect('exapp:home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('exapp:login')
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


#edit profile # 
def edit_profile(request):
    current_user = get_object_or_404(User, username=str(request.user))
    user = User.objects.filter(user=current_user)
    data = Profile.objects.filter(user=current_user)
    if request.method == "POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        age=request.POST['age']
        city=request.POST['city']
        gender=request.POST['gender']
        user=User.objects.create(first_name=first_name,last_name=last_name,email=email)
        user.save()
        data =Profile.objects.create(contact_number=contact,age=age,city=city,gender=gender)
        data.save()

        return render(request,"exapp/editprofile.html",{'user':user, 'data':data})
    else:
        return render(request,"exapp/editprofile.html", {'user':user, 'data':data})


# acconnt information  section #
def account(request):
    current_user = get_object_or_404(User, username=str(request.user))
    data = Profile.objects.filter(user=current_user)
    record =  User.objects.all()
    kycs = kyc.objects.filter(user=current_user)
    return render(request,'exapp/acc.html',{'record':record,'kycs':kycs,'data':data})

# transcations #

def orders(request):
    current_user = get_object_or_404(User, username=str(request.user))
    orders = CurrencyOrder.objects.filter(user=current_user)
    kycs = kyc.objects.filter(user=current_user)
    return render(request,'exapp/orders.html',{'orders':orders,'kycs':kycs, 'current_user':current_user})



# buying currency part #

def buy(request):

    if request.method == 'POST':
        currency_from = request.POST['currency_from']
        currency_to = request.POST['currency_to']
        forex_amount = request.POST['forex_amount']

        if currency_from=='select' and currency_to == 'select':
            messages.error(request,'Select Desired Currency')
            return redirect('exapp:buy')

        if currency_from == 'USD':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            forex_rate = data['USD_INR']
            inr_amount = forex_rate * float(forex_amount)
            Commission_amount= inr_amount * 0.03
            total_amount = inr_amount + Commission_amount
            
        elif currency_from == 'euro':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=EUR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            forex_rate = data['EUR_INR']
            inr_amount = forex_rate * float(forex_amount)
            Commission_amount= inr_amount * 0.03
            total_amount = inr_amount + Commission_amount

        elif currency_from == 'Dirham':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=MAD_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            forex_rate = data['MAD_INR']
            inr_amount = forex_rate * float(forex_amount)
            Commission_amount= inr_amount * 0.03
            total_amount = inr_amount + Commission_amount

        elif currency_from == 'Yuan':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=CNY_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            forex_rate = data['CNY_INR']
            inr_amount = forex_rate * float(forex_amount)
            Commission_amount = inr_amount * 0.03
            total_amount = inr_amount + Commission_amount
        
        elif currency_from == 'pkr':
            res = requests.get("https://free.currconv.com/api/v7/convert?q=PKR_INR&compact=ultra&apiKey=8ae59ce2eb49edbce982")
            data = res.json()
            forex_rate = data['PKR_INR']
            inr_amount = forex_rate * float(forex_amount)
            Commission_amount= inr_amount * 0.03
            total_amount = inr_amount + Commission_amount

       

        currency = CreateOrder.objects.create(user=request.user,currency_from=currency_from,currency_to=currency_to,forex_amount=forex_amount,inr_amount=inr_amount,total_amount=total_amount,Commission_amount=Commission_amount,forex_rate=forex_rate)
        currency.save()
        # return render(request,'exapp/confirmorder.html')
        return redirect('exapp:confirmorder')
        
    else:
        return render(request,'exapp/buy.html')




# conifrm order 

def confirm_order(request):
    current_user = get_object_or_404(User, username=str(request.user))
    order = CreateOrder.objects.filter(user=current_user).order_by("-id")[0]

    if request.method == "POST":
        if  order.inr_amount > 10000 and  ( order.inr_amount % 500 ):
            currency=CurrencyOrder.objects.create(user=current_user,currency_from=order.currency_from,currency_to=order.currency_to,forex_amount=order.forex_amount,inr_amount=order.inr_amount,total_amount=order.total_amount,Commission_amount=order.    Commission_amount,forex_rate=order.forex_rate)
            currency.save()
            return redirect('exapp:pay')
        else:
            messages.error(request,'INR Amount must be greater than 10,000 INR and multiples of 500 ....!')
            return redirect('exapp:buy')
    else:
        return render(request,'exapp/confirmorder.html',{'order':order,'current_user':current_user})


    
    
# kyc section #

def kyc_add(request):
    current_user = get_object_or_404(User, username=str(request.user))
    kycs = kyc.objects.filter(user=current_user)

    if request.method == 'POST':
        pancard = request.FILES['pancard']
        aadhar = request.FILES['aadhar']

        if kyc.objects.filter(aadhar=aadhar).exists():
            messages.error(request,' Aadhar Already Exists')
            return redirect(request,'exapp:kyc')
        elif kyc.objects.filter(pancard=pancard).exists():
            messages.error(request,' Pancard Already Exists')
            return redirect(request,'exapp:kyc')

        elif request.FILES['aadhar'] is None:
            messages.error(request,' Attach Your Aadhar')
            return redirect(request,'exapp:kyc')

        elif request.FILES['pancard'] is None:
            messages.error(request,' Attach Your Pancard')
            return redirect(request,'exapp:kyc')

        else:
            doc1 = kyc.objects.create(user=request.user,aadhar=aadhar,pancard=pancard)
            messages.info(request,"Document Uploaded  Sucessfully")
            return redirect('exapp:kyc')
    
        return redirect('exapp:kyc')
    else:
        return render(request,'exapp/kyc.html', {'kycs':kycs})
    return render(request,'exapp/kyc.html', {'kycs':kycs})
           

    
        
    

# payment section #


# def payment_process(request):
#     order_id = request.session.get('order_id')
#     order = get_object_or_404(order,id=order_id)
#     host=request.get.host()

#     paypal_dict={
#         'bussiness' : settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '%2f' % order.get_inr_amount
#         iten_name
#     }

def pay(request):
    current_user = get_object_or_404(User, username=str(request.user))
    order=CurrencyOrder.objects.filter(user=current_user).order_by("-id")[0]
    if request.method == 'POST':
        order_amount ='{{ order.inr_amount}}'
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_KqegTBbnvoPiap','BzvLi7pjKrx8TGpWz3R6F6nm'))
        payment = client.order.create({'amount':amount,'currency': 'INR', 'payment_capture':'1'})
    return render(request,'exapp/pay.html',{'current_user':current_user,'order':order})


# sucess page after payment #
@csrf_exempt
def success(request):
    
    return render(request,'exapp/success.html')



def transcation(request):
    return render(request,'exapp/transcation.html')


