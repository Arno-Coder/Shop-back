from django.http import JsonResponse

from product.models import Product


def product_list(request):
    products = Product.objects.filter(is_active=True, quantity__gt=0)
    data = {
        'products': list(products.values())
    }
    return JsonResponse(data)