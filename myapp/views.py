from django.shortcuts import render,redirect
from django.views import View
from .models import CustomerModel,ProductModel,CartModel,OrderPlacedModel
from .forms import SignupForm,LoginForm,CustomerForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout



class home(View):
    def get(self,request):
        NewArrivals = ProductModel.objects.filter(category='N')
        Featured = ProductModel.objects.filter(category='F')
        d = {'newarrivals':NewArrivals,'featured':Featured}
        return render(request,'home.html',d)


# __________________Categories____________________________________

def menswear(request):
    menswear = ProductModel.objects.filter(category='M')
    return render(request,'menswear.html',{'menswear':menswear})

def womenswear(request):
    womenswear = ProductModel.objects.filter(category='W')
    return render(request,'womenswear.html',{'womenswear':womenswear})

def accessories(request):
    accessories = ProductModel.objects.filter(category='A')
    return render(request,'accessories.html',{'accessories':accessories})
    



class signup(View):
    def get(self,request):
        form = SignupForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        User.objects.create_user(username=username,email=email,password=password)
        form.save()
        return redirect('login')
        
            
class ProductDeatils(View):
    def get(self,request,pk):
        product = ProductModel.objects.get(pk=pk)
        return render(request,'productdetails.html',{'product':product})

class login(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return redirect('login')

def logout(request):
    auth_logout(request)
    return redirect('home')


class address(View):
    def get(self,request):
        form = CustomerForm()
        return render(request,'address.html',{'form':form})
    def post(self,request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            username = request.user
            name = form.cleaned_data['name']   
            phone = form.cleaned_data['phone']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            register = CustomerModel(username=username,name=name,phone=phone,
            locality=locality,city=city,zipcode=zipcode)
            register.save()
        return redirect('profile')

# _________________profile____________________________

def profile(request):
    add = CustomerModel.objects.filter(username = request.user)
    return render(request,'profile.html',{'add':add})

def add_delete(request,id):
    add_delete = CustomerModel.objects.get(id=id)
    add_delete.delete()
    return redirect('profile')

def add_edit(request,id):
    add_edit = CustomerModel.objects.get(id=id)
    if request.method == 'POST':
        add = CustomerForm(request.POST,instance=add_edit)
        add.save()
        return redirect('profile')
    form = CustomerForm(instance=add_edit)
    return render(request,'address.html',{'form':form})


# __________________order___________________________

def order(request):
    user = request.user
    op = OrderPlacedModel.objects.filter(user=user)
    return render(request,'order.html',{'op':op})

def ordersuccess(request):
    return render(request,'ordersuccess.html')



# ___________________cart__________________________________

def add_to_cart(request):
    username = request.user
    product_id = request.GET.get('product_id')
    product = ProductModel.objects.get(id=product_id)
    cart = CartModel(user=username,product=product)
    cart.save()
    return redirect('cart')


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = CartModel.objects.filter(user=user)
        amt = 0.0
        shipping_amt = 50
        tax = 50
        total_amt = 0.0
        cart_product = [p for p in CartModel.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp_amt = (p.quantity * p.product.price)
                amt += temp_amt
                total_amt = amt + shipping_amt + tax
            return render(request,'cart.html',{'cart':cart,'total_amt':total_amt,'amt':amt})
        else:
            return render(request,'emptycart.html')

def cart_delete(reqeust,id):
    c_delete = CartModel.objects.get(id=id)
    c_delete.delete()
    return redirect('cart')





class checkout(View):
    def get(self,request):
        user = request.user
        address = CustomerModel.objects.filter(username=user)
        cart_items = CartModel.objects.filter(user=user)
        print(cart_items)
        amt = 0.0
        shipping_amt = 50
        tax = 50
        total_amt = 0.0
        cart_product = [p for p in CartModel.objects.all() if p.user == user]
        if cart_product:
            for p in cart_product:
                temp_amt = (p.quantity * p.product.price)
                amt += temp_amt
                total_amt = amt + shipping_amt + tax
            
        return render(request,'checkout.html',
            {
            'address':address,
            'cart_items':cart_items,
            'total_amt':total_amt,
            'amt':amt
            }
        )

class payment(View):
    def get(self,request):
        user = request.user
        custid = request.GET.get('custid')
        customer = CustomerModel.objects.get(id=custid)
        cart = CartModel.objects.filter(user=user)
        for i in cart:
            order = OrderPlacedModel(user=user, customer=customer, product=i.product,
            quantity=i.quantity)
            order.save()
            i.delete()
        return render(request,'payment.html')