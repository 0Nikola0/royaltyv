from django.urls import path
from . import views

urlpatterns = [
    path('', views.trending_movies, name="trending_movies"),      # Tuka treba da staam home page a ne direkt movies da ode
    path('movies/', views.trending_movies, name="trending_movies"),
    path('tv-shows/', views.trending_tvs, name="trending_tvs"),
    # Searched
    path('movies', views.search_movies, name="search_movies"),
    path('tv-shows', views.search_tvs, name="search_tvs"),
    # Clicked on
    path('movies?<movie_id>', views.selected_movie, name="selected_movie"),
    path('tv-shows?<tv_id>', views.selected_tv, name="selected_tv"),
    # Registration
    path('register/', views.registration, name="registration"),
    path('login/', views.registration, name="login"),
]
 