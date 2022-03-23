from io import BytesIO
from typing import Union

import requests
from PIL import Image

urlwallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/wallpaper'
urlmoviewallpaperjson = 'https://micswallpaperapi.herokuapp.com/json/Film_TV_Wallpaper'

def Wallpapersimagelink():
    response = requests.get(urlwallpaperjson)
    response = response.json()
    return response['img_url']

def wallpapersimage() -> Image:
    response = requests.get('https://micswallpaperapi.herokuapp.com/wallpaper')
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)



class Wallpaper():
    BASE_URL = "https://micswallpaperapi.herokuapp.com"

    @classmethod
    def movie_wallpaper(cls, json_data = False) -> Union[Image.Image, dict]:
        if json_data:
            url = f"{cls.BASE_URL}/json/Film_TV_Wallpaper"
            response = requests.get(url)
            result = response.json()
            
            return result
            
        else:
            url = f"{cls.BASE_URL}/Film_TV_Wallpaper"
            response = requests.get(url)
            image_data = response.content

            image = BytesIO(image_data)
            image.seek(0)

            result = Image.open(image)

            return result
        