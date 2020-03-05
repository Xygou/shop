from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *

def shop(request):
    name = 'Velikdus Igor'
    current_day = "02.03.2020"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data ['name'])

        new_form = form.save()

    return render(request, 'shop/shop.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    return render(request, 'shop/home.html', locals())
