import requests
from io import BytesIO
from PIL import Image

urlwallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/wallpaper'
urlmoviewallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/Film_TV_Wallpaper'

def Wallpapersimagelink():
    response = requests.get(urlwallpaperjson)
    response = response.json()
    return response['img_url']

def filmimagelink():
    response = requests.get(urlmoviewallpaperjson)
    response = response.json()
    return response['img_url']


def wallpapersimage() -> Image:
    response = requests.get('https://micswallpaperapi.herokuapp.com/wallpaper')
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)
