from django.shortcuts import render
from .models import Product
from django.utils import timezone

# Create your views here.


def post_list(request):
    products = Product.objects.filter(added_date__lte = timezone.now()).order_by('added_date')
    return render(request, 'product_lister/post_list.html', {'products':products})
