from django.shortcuts import render
from .models import *

# Create your views here.
def erp(request):
    return render(request, 'app/erp.html')

def home(request):
    return render(request, 'app/index.html')

def project(request):
    image = Projects.objects.all()
    return render(request, 'app/projects.html',{"image":image})

def products(request):
    return render(request, 'app/products.html')

def subproducts(request,type):
    product = Products.objects.filter(typeOfProduct=type)
    return render(request, 'app/subproducts.html',{"product":product})

def productdescription(request,id):
    product = Products.objects.get(id=id)
    return render(request, 'app/productdescription.html',{"product":product})


def aboutus(request):
    return render(request, 'app/aboutus.html')

def contact(request):
    return render(request, 'app/contact.html')