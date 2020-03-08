from django.shortcuts import render,redirect
from .models import Category
from .forms import CategoryForm

# Create your views here.
def all(request):
    return render(request,"category/all.html",{"cats":Category.objects.all()})

def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save() 
            return redirect("/cat/")
    else : 
        form = CategoryForm()
    return render(request,"category/create.html",{"form":form})
def edit(request,id):
    instance = Category.objects.get(id=id)
    if request.method=="POST":
        form=CategoryForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/cat/')
    else:
        form=CategoryForm(instance=instance)
    #return render(request,"category/edit.html")
    return render(request,"category/edit.html",{"form":form})
def delete(request,id,name):
    Category.objects.get(id=id).delete()
    return redirect('/cat/')