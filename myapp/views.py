from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import admin
from .models import productt,userr,CartItem,wishlist
import os
import sweetify
from django.views import View
from django.shortcuts import redirect,reverse
# Create your views here.
signup_data = {}
def loginPage_shopkeeper(request):
    if request.method=='POST':
        shopkeepername=request.POST.get('username')
        print("llllll",shopkeepername)
        password1=request.POST.get('password')
        #print(shopkeeper, password1)
        print('stored_password',password1)
        data_user = authenticate(username=shopkeepername,password=password1)
        print('sssssssssssssssss',data_user)
        if data_user is not None:
            return redirect('add_page')
        else:
            print("llllllllll")
    return render(request,'login.html')


#user registration and login 

signup_data = {}
def signupPage_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        userimage=request.FILES.get('userimage')
        print("lllllll",userimage)
        userphone=request.POST.get('phonenumber')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("Password and confirm password are not same")
        else: 
          #signup_data[username] = password1
          #print(signup_data)
          print('username',userimage,username,password1,password2)
          my_user=userr.objects.create(user_image=userimage,user_name=username,user_phone=userphone)
          my_user.save()
          
          return redirect('login_user')
          #return HttpResponse("teacher data as been entered succesfully")
    return render(request,'signin_user.html')

def loginPage_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password')
        x = CartItem.objects.all()
        y= wishlist.objects.all()
        y.delete()
        x.delete()
        #stored_password = signup_data.get(username)
        print(username, password1)
        #print('stored_password',stored_password)
        try:
            data = userr.objects.get(user_name=username)
            request.session['user_data'] = username    #if the user is unique
            sweetify.success(request, 'successfuly entered')
            return redirect('home')
        except:
            sweetify.error(request, 'Enter valid username and password')
            return redirect('/login_user/')
         
        # if stored_password == password1:
        #     return redirect('home')
        # else:
        #     return HttpResponse("Username Or Password is incorrect")

        #     ############################
        #     if hospitalname=='hospital_1':
        #       return redirect('adding_doc_patients')
        #     elif  hospitalname=='hospital_2':
        #       return redirect('adding_doc_patients1')
        #     elif hospitalname=='hospital_3':
        #       return redirect('adding_doc_patients2')
        # else:
        #     return HttpResponse("Username Or Password is incorrect")

    return render(request,'login_user.html')


def add_data_page(request):
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'add_shopkeeper':
                productname=request.POST.get('productname')
                try:
                  productimage=request.FILES.get('image1')
                except:
                  productimage=""
                productimage=request.FILES.get('productimage')
                productprice= request.POST.get('productprice')
                productcategory= request.POST.get('productcategory')
                prod=productt.objects.create(product=productname,image=productimage,price=productprice,category=productcategory)
                prod.save()
    return render(request,'add_page.html')

# PRODUCT VIEW

def new(request):
        
        if request.method == 'POST':
            p1= request.POST.get('l_shirt')
            p2= request.POST.get('l_skert')
            p3=request.POST.get('m_shirt')
            p4=request.POST.get('m_trouser')
            print('bag111',p1)
            print('cat111',p2)
            print('dog111',p3)
            if p1=='l_shirt':
                return redirect('/add_page1/')
            elif p2=='l_skert':
                return redirect('/add_page2/')
            elif p3=='m_shirt':
                return redirect('/add_page3/')
            elif p4=='m_trouser':
                return redirect('/add_page4/')

        # bag = productt.objects.filter(category='bag')
        # cat = productt.objects.filter(category='cat')
        # data_user = request.session['user_data']
        # print("lllllllllllll",data_user)
        return render(request, 'home.html')
                    
def add_page1(request):  
    l_shirt = productt.objects.filter(category='l_shirt')
    l_skert = productt.objects.filter(category='l_skert')
    m_shirt= productt.objects.filter(category='m_shirt')
    context={'l_shirt': l_shirt,'l_skert':l_skert,'m_shirt':m_shirt}
    return render(request, 'add_page1.html',context)
             
def add_page2(request):  
    l_shirt = productt.objects.filter(category='l_shirt')
    l_skert = productt.objects.filter(category='l_skert')
    m_shirt= productt.objects.filter(category='m_shirt')
    context={'l_shirt': l_shirt,'l_skert':l_skert,'m_shirt':m_shirt}
    return render(request, 'add_page2.html',context)
             
def add_page3(request):  
    l_shirt = productt.objects.filter(category='l_shirt')
    l_skert = productt.objects.filter(category='l_skert')
    m_shirt= productt.objects.filter(category='m_shirt')
    context={'l_shirt': l_shirt,'l_skert':l_skert,'m_shirt':m_shirt}
    return render(request, 'add_page3.html',context)

def add_page4(request):  
    l_shirt = productt.objects.filter(category='l_shirt')
    l_skert = productt.objects.filter(category='l_skert')
    m_shirt= productt.objects.filter(category='m_shirt')
    m_trouser= productt.objects.filter(category='m_trouser')
    context={'l_shirt': l_shirt,'l_skert':l_skert,'m_shirt':m_shirt,'m_trouser':m_trouser}
    return render(request, 'add_page4.html',context)

######################################################################

# To view the added cart items
def view_cart(request):
    cart_items = CartItem.objects.filter(user_id=request.user.id)
    total_price = sum(int(item.product.price) * int(item.quantity) for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

# To add the cart items
def add_to_cart(request,product_id):
    if request.method == 'POST':  ########
        # product_id = request.POST.get('product_id')
        product = productt.objects.get(id=product_id)  #use to acess perticular product using product_id
        print('dddddddddddddddddddddddddddddddddddddddddddd',product_id)
        cart_item, created = CartItem.objects.get_or_create(product_id=product_id, user_id=request.user.id)
        cart_item.user_name=request.session['user_data']
        quantity = int(request.POST.get('quantity', 1)) ###########
        print('^^^^^^^^^&&&&&&&&&&&&&&^^^^^^^^^',quantity)
        cart_item.quantity=quantity
        # cart_item.quantity += 1
        cart_item.total_price=cart_item.quantity*cart_item.product.price
        cart_item.save()
    #to come back to same page
    referer = request.META.get("HTTP_REFERER", None)
    return redirect(referer)

# To remove the cart items
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('/cart/')

# To view the added cart items
def view_wishlist(request):
    wishlist_items = wishlist.objects.filter(user_id=request.user.id)
    return render(request, 'wishlist.html',{'wishlist_items': wishlist_items})

def add_wishlist(request, product_id):
    product = productt.objects.get(id=product_id)  #use to acess perticular product using product_id
    wishlist_item, created = wishlist.objects.get_or_create(product_id=product_id, user_id=request.user.id)
    referer = request.META.get("HTTP_REFERER", None)
    return redirect(referer)
# def base_page(request):
#    return render(request, "demo_base.html")

def orders(request):
    oder= CartItem.objects.all()
    return render(request, 'order.html',{'order_items': oder}) 

def payment(request):
    data=request.session['user_data']
    cart_items = CartItem.objects.filter(user_id=request.user.id)
    total_price = sum(int(item.product.price) * int(item.quantity) for item in cart_items)
    if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'action_payment':
                  return HttpResponse("payment done sucessfully")
            
    return render(request, 'payment.html', {'data':data,'cart_items': cart_items, 'total_price': total_price})

def logoutuser(request):
    request.session['user_data']=''
    return redirect('/login_user/')