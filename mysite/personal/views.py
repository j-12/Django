from django.shortcuts import render
from .models import Product, Cart, user_info
from django.http import HttpResponse, HttpResponseRedirect
from django.db import IntegrityError

# data=info.objects.all()


product_data = Product.objects.all()


def index(request):
    return render(request, 'personal/home.html')


# def contact(request):
# 	return render(request,'personal/basic.html',{'content':['If you would like to contact me, please email me.','somilshah112@gmail.com']})
# # Create your views here.
# def information(request):
# 	return render(request,'personal/basic.html',{'content':data})

def products(request):
    return render(request, 'personal/products.html', {'content': product_data})


def add_to_cart(request):
    if 'cart' in request.POST:
        product_id = request.POST.get('cart', '')
        product = Product.objects.get(id=product_id)
        name = product.product_name
        amount = product.product_price
        addToCart = Cart.objects.create(cart_product_name=name, cart_product_price=amount)
        addToCart.save()
        return render(request, 'personal/successful.html', {'content': [name, ]})

    else:
        username = 'You submitted an empty form.'
        return HttpResponse(username)


def viewcart(request):
    if 'clear' in request.POST:
        Cart.objects.all().delete()
        cart_data2 = Cart.objects.all()
        return render(request, 'personal/viewcart.html', {'content': cart_data2})
    cart_data = Cart.objects.all()
    return render(request, 'personal/viewcart.html', {'content': cart_data})


def login(request):
    if 'register' in request.POST:
        if 'uname' in request.POST:
            username = request.POST.get('uname', '')
        else:
            username = 'You submitted an empty form.'
        if 'password' in request.POST:
            password = request.POST.get('password', '')
        try:
            user = user_info.objects.create(name=username, password=password)
            user.save()
            return HttpResponse(
                "<h2>User:  " + username + "<br> Password:   " + password + " <br>Registered successfully</h2>")
        except IntegrityError as e:
            if 'UNIQUE' in e.args[0]:
                return HttpResponse("Username already exists, please choose a different username")

    if 'signin' in request.POST:
        if 'uname' in request.POST:
            username = request.POST.get('uname', '')
            password = request.POST.get('password', '')
            try:
                user_object = user_info.objects.get(name=username)
            except user_info.DoesNotExist:
                user_object = None
                return HttpResponse("User does not exist")

            if (user_object != None):
                user_auth = user_object.name
                password_auth = user_object.password
                return HttpResponseRedirect("/products/")
            else:
                return HttpResponse("User does not exist")
            # if user_object is None:
            #     return HttpResponse('No such User')
            # elif username == user_auth and password == password_auth:
            #     return HttpResponse('Successfully logged in')
            # else:
            #     return HttpResponse('Invalid username or password')
