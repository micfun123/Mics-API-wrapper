from io import BytesIO
from typing import Union

import requests
from PIL import Image


class Wallpaper():
    BASE_URL = "https://micswallpaperapi.herokuapp.com"

    @classmethod
    def movie_wallpaper(cls, json_data = False) -> Union[Image.Image, dict]:
        if json_data:
            url = f"{cls.BASE_URL}/json/Film_TV_Wallpaper"
            response = requests.get(url)
            result: dict = response.json()
            
            return result
            
        else:
            url = f"{cls.BASE_URL}/Film_TV_Wallpaper"
            response = requests.get(url)
            image_data = response.content

            image = BytesIO(image_data)
            image.seek(0)

            result: Image.Image = Image.open(image)

            return result


    @classmethod
    def wallpaper(cls, json_data = False) -> Union[Image.Image, dict]:
        if json_data:
            url = f"{cls.BASE_URL}/json/wallpaper"
            response = requests.get(url)
            
            result: dict = response.json()
            
            return result
            
        else:
            url = f"{cls.BASE_URL}/wallpaper"
            response = requests.get(url)
            image_data = response.content

            image = BytesIO(image_data)
            image.seek(0)

            result: Image.Image = Image.open(image)

            return result