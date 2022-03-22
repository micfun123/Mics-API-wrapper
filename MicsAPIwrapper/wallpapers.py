import requests

urlwallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/wallpaper'

def getWallpapersimagelink():
    response = requests.get(urlwallpaperjson)
    response = response.json()
    return response['img_url']

