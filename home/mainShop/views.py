from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json


def about(request):
    return render(request, 'mainShop/about.html')


def index(request):
    prodArr = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n = len(product)
        slideNo = n // 4 + ceil((n / 4) - (n // 4))
        prodArr.append([product, range(1, slideNo), slideNo])
    passer = {'prodArr': prodArr}
    return render(request, 'mainShop/index.html', passer)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'mainShop/help.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Your Order has been placed successfully!")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'mainShop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'mainShop/checkout.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
            
    return render(request, 'mainShop/tracker.html')

def prodView(request, myId):
    product = Product.objects.filter(id=myId)
    return render(request, 'mainShop/prodView.html', {'product':product[0]})

