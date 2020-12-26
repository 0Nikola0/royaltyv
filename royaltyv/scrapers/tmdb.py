import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
IMG_BASE_URL = "https://image.tmdb.org/t/p/w154/"


def getTrending(MorTV):
    '''
    MorTV:
        - type: string,
        - value: 'movie' for movies, 'tv' for tv shows
    Returns: list of json-s
    '''
    TRENDING_URL = f"https://api.themoviedb.org/3/trending/{MorTV}/day?api_key={API_KEY}"
    response = requests.request("GET", TRENDING_URL)
    data = response.json()
    data = data["results"]
    return data


def getSearched(MorTV, searched):
    '''
    MorTV:
        - type: string,
        - value: 'movie' for movies, 'tv' for tv shows
    searched: 
        - type: string,
        - value: what the user searched for
    Returns: list of json-s
    '''
    SEARCHED_URL = f"https://api.themoviedb.org/3/search/{MorTV}?api_key={API_KEY}&query={searched}&page=1&include_adult=true"
    response = requests.request("GET", SEARCHED_URL)
    data = response.json()
    data = data["results"]
    return data
    

def getSelected(MorTV, MorTV_ID):
    '''
    MorTV:
        - type: string,
        - value: 'movie' for movies, 'tv' for tv shows
    MorTV_ID: 
        - type: string / integer,
        - value: ID of the selected movie / tv show
    Returns: list of json-s
    '''
    SEARCHED_URL = f"https://api.themoviedb.org/3/{MorTV}/{str(MorTV_ID)}?api_key={API_KEY}&language=en-US"
    response = requests.request("GET", SEARCHED_URL)
    data = response.json()
    data = data
    return data
