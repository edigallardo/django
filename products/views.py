from django.shortcuts import render
from products.models import Product
from django.http import HttpResponse

def get_product(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        return render(request, 'product/product.html', context={'product': product})

    except Product.DoesNotExist:
        # Manejar el caso donde el producto no existe
        return HttpResponse("El producto no fue encontrado.", status=404)

    except Exception as e:
        # Manejar otras excepciones de manera adecuada (puedes personalizar según tus necesidades)
        print(e)
        return HttpResponse("Error interno del servidor", status=500)