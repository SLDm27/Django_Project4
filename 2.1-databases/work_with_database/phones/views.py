from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get("sort")
    phone_instanse = Phone.objects.all()
    if sort_pages == "name":
        phone_instanse = Phone.objects.order_by("name")
    elif sort_pages == "max_price":
        phone_instanse = Phone.objects.order_by("price").reverse()
    elif sort_pages == "min_price":
        phone_instanse = Phone.objects.order_by("price")
    context = {"phones": phone_instanse}
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context=context)