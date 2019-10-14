from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact
from math import ceil


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    params = {'allProds': allProds}
    return render(request, 'mainShop/index.html', params)


def about(request):
    return render(request, 'mainShop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'mainShop/help.html')


def tracker(request):
    return render(request, 'mainShop/tracker.html')


def search(request):
    return render(request, 'mainShop/search.html')


def prodView(request, myId):
    product = Product.objects.filter(id=myId)
    return render(request, 'mainShop/prodView.html', {'product':product[0]})


def checkout(request):
    return render(request, 'mainShop/checkout.html')