from mywatchlist.models import MyWatchlist
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_html(request):
    watchlist_data = MyWatchlist.objects.all()
    number_of_watched_films = len([film for film in watchlist_data if film.watched])
    banyak_menonton = number_of_watched_films >= len(watchlist_data) - number_of_watched_films
    context = {
        'watchlist': watchlist_data,
        'nama': 'Nadya Hoesin',
        'npm': '2106651673',
        'pesan': 'Selamat, kamu sudah banyak menonton!' if banyak_menonton else 'Wah, kamu masih sedikit menonton!'
    }

    return render(request, "mywatchlist.html", context)

def show_json(request):
    watchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", watchlist_data), content_type="application/json")

def show_xml(request):
    watchlist_data = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", watchlist_data), content_type="application/xml")



