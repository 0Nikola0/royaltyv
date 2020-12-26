from django.shortcuts import render
from django.http import HttpResponse

from .scrapers.tmdb import IMG_BASE_URL
from .scrapers.tmdb import getTrending, getSearched, getSelected


def trending_movies(request):
    data = getTrending("movie")
    context = {
        "data": data,
        "img_base_url": IMG_BASE_URL
    }
    return render(request, "royaltyv/home/movies.html", context)


def trending_tvs(request):
    data = getTrending("tv")
    context = {
        "data": data,
        "img_base_url": IMG_BASE_URL
    }
    return render(request, "royaltyv/home/tv-shows.html", context)

# Searched pages
def search_movies(request):
    if request.method == "GET":
        searched = request.GET.get("search")
        print(searched)
        
        data = getSearched("movie", searched)
        context = {
            "data": data,
            "img_base_url": IMG_BASE_URL
        }
        return render(request, "royaltyv/home/movies.html", context)


def search_tvs(request):
    if request.method == "GET":
        searched = request.GET.get("search")
        print(searched)
        
        data = getSearched("tv", searched)
        context = {
            "data": data,
            "img_base_url": IMG_BASE_URL
        }
        return render(request, "royaltyv/home/tv-shows.html", context)


def selected_movie(request, movie_id):
    if request.method == "GET":
        
        data = getSelected("movie", movie_id)
        context = {
            "data": data,
            "img_base_url": IMG_BASE_URL
            }

        return render(request, "royaltyv/home/selected-movie.html", context)


def selected_tv(request, tv_id):
    if request.method == "GET":
        
        data = getSelected("tv", tv_id)
        context = {
            "data": data,
            "img_base_url": IMG_BASE_URL
            }

        return render(request, "royaltyv/home/selected-tv.html", context)
        
