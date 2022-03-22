import requests

urlwallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/wallpaper'
urlmoviewallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/wallpaper'

def Wallpapersimagelink():
    response = requests.get(urlwallpaperjson)
    response = response.json()
    return response['img_url']

def filmimagelink():
    response = requests.get(urlmoviewallpaperjson)
    response = response.json()
    return response['img_url']

