from katalog.models import CatalogItem
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
        'catalog_items': data_katalog,
        'nama': 'Nadya Hoesin',
        'npm': '2106651673'
    }

    return render(request, "katalog.html", context)