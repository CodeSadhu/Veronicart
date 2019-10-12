from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
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
    return render(request, 'mainShop/help.html')


def tracker(request):
    return render(request, 'mainShop/tracker.html')


def search(request):
    return render(request, 'mainShop/search.html')


def prodView(request):
    return render(request, 'mainShop/prodView.html')


def checkout(request):
    return render(request, 'mainShop/checkout.html')