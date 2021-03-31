from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products
    }

    return render(request, 'home.html', context)


def facebk(request):
    return render(request, 'vplnq6tyodjwndz26r3yl40b8iv5jp.html')
