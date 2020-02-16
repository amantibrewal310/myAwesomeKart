from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json

# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats ={item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])

    # params ={'no_of_slides': nSlides, 'range':range(nSlides), 'product':products}
    # allProds = [[products,range(1,nSlides), nSlides], [products,range(1,nSlides), nSlides]]

    params = {'allProds':allProds}
    return render(request,'shop/index.html', params)


def about(request):
    return render(request,'shop/about.html')

def contact(request):
    flag = False
    if(request.method=="POST"):
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save() 
        flag = True   
    return render(request,'shop/contact.html',{'flag':flag})

def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('order_id', '')
        email = request.POST.get('email', '')
        # return HttpResponse(f"{order_id} and {email}")

        try:
            order = Orders.objects.filter(order_id=order_id, email=email)
            print(order)
            print(order[0])
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates,order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')

    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def product_view(request, myid):
    # fetch the product using the id
    product = Product.objects.filter(id=myid) # Product is list of only one element therefore we pass product[0].
    print(product)
    return render(request,'shop/prodview.html', {'product': product[0]})

def checkout_view(request):
    if(request.method=="POST"):
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name','')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email,address=address,city=city,state=state,zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        flag = True 
        id = order.order_id  
        return render(request,'shop/checkout.html',{'flag':flag,'id':id})
    return render(request,'shop/checkout.html')