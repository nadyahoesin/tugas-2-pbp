from mywatchlist.models import MyWatchlist
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_html(request):
    watchlist_data = MyWatchlist.objects.all()
    context = {
        'watchlist': watchlist_data,
        'nama': 'Nadya Hoesin',
        'npm': '2106651673'
    }

    return render(request, "mywatchlist.html", context)

def show_json(request):
    watchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist_data), content_type="application/json")

def show_xml(request):
    watchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist_data), content_type="application/xml")



