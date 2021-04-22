from django.shortcuts import render,redirect
from .models import Brands,Mobile,Orders
from mobile.forms import BrandCreateform,BrandUpdateForm,MobileCreateForm,OrderForm
from .forms import UserRegForm,User
from django.contrib.auth import authenticate,login,logout

# Create your views here
def admin_permission_required(func):
    def wrapper(request):
        if not request.user.is_superuser:
            return redirect("errorpg")
        else:
            return func(request)
    return wrapper

def admin_permission_del_upd(func):
    def wrapper(request,id):
        if not request.user.is_superuser:
            return redirect("errorpg")
        else:
            return func(request,id)
    return wrapper


@admin_permission_required
def create_brand(request):
    form=BrandCreateform()
    context={}
    context['form']=form
    brands=Brands.objects.all()
    context["brands"]=brands
    if request.method=="POST":
        form=BrandCreateform(request.POST)
        if form.is_valid():
            form.save()
            print("brand saved")
            return redirect("brands")
        else:
            form=BrandCreateform(request.POST)
            context={}
            return redirect("brands")
            # return render(request,'mobile/brandcreate.html',context)
    return render(request,"mobile/brandcreate.html",context)

@admin_permission_del_upd
def brand_delete(request,id):
    brand=Brands.objects.get(id=id)
    brand.delete()
    return redirect("brands")

@admin_permission_del_upd
def brand_update(request,id):
    brand=Brands.objects.get(id=id)
    form=BrandUpdateForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandUpdateForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("brands")
        else:
            return render(request,"mobile/brandedit.html",context)
    return render(request,"mobile/brandedit.html",context)

@admin_permission_required
def create_mobile(request):
    if request.user.is_superuser:
        form=MobileCreateForm()
        context={}
        context["form"]=form
        if request.method=="POST":
            form=MobileCreateForm(request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                print("saved")
                return redirect("createmobile")
        return render(request,"mobile/mobilecreate.html",context)
    else:
        return redirect("userlogin")

def errorpg(request):
    return render(request,"mobile/errorpage.html")

def list_mobiles(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobiles.html",context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetail.html",context)

def user_registration(request):
    form=UserRegForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("userlogin")
        else:
            form=UserRegForm(request.POST)
            context["form"]=form
            return render(request, "mobile/userreg.html", context)
    return render(request,"mobile/userreg.html",context)

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pwd")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("listmobiles")
        else:
            return render(request, "mobile/login.html")

    return render(request,"mobile/login.html")

def user_logout(request):
    logout(request)
    return redirect("userlogin")
# 'user':request.user,

def order(request,id):
    product = Mobile.objects.get(id=id)
    username= request.user
    form=OrderForm(initial={'product':product,'user':username})
    context={}
    context['form']=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        print("test point")
        if form.is_valid():
            form.save()
            return redirect("cart")
        else:
            form=OrderForm(request.POST)
            context["form"]=form
            return render(request, "mobile/orders.html", context)
    return render(request,"mobile/orders.html",context)

def cart(request):
    userna=request.user
    orders=Orders.objects.filter(user=userna)
    print(orders)
    context = {}
    context["orders"]=orders
    return render(request,"mobile/cart.html",context)

def cancel(request,id):
    orders=Orders.objects.get(id=id)
    orders.delete()
    return redirect("cart")

def view_order(request,id):
    orders=Orders.objects.get(id=id)
    context={}
    context["orders"] = orders
    return render(request,'mobile/vieworders.html',context)
