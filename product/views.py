from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request,"product/home.html",{"pros":Product.objects.all()})
def create(request):
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pro-home')
    else:
        form=ProductForm()
    return render(request,"product/creat.html",{"form":form})
def edit(request,id):
    instance=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('pro-home')
    else:
        form=ProductForm(instance=instance)
    return render(request,'product/edit.html',{"form":form})
def delete(request,id):
    Product.objects.get(id=id).delete()
    return redirect('pro-home')
