from io import BytesIO
from typing import Union

import requests
from PIL import Image


class Wallpaper():
    # Base API url
    BASE_URL = "https://micswallpaperapi.herokuapp.com"


    @classmethod
    def wallpaper(cls, json_data = False) -> Union[Image.Image, dict]:
        """
        This function will return a random wallpaper either as a Pil.Image.Image or a dict

        Parameters
        ----------
            :param json_data (bool, Optional) : If this is set to `True` the function will return the response 
                as a json/dict. If set to `False` it will return a `PIL.Image.Image` image

        Returns 
        -------
            Union[Image.Image, dict]: 
                If the param (json_data) is True it will return dict else PIL.Image.Image
                
        """
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

    
    @classmethod
    def movie_wallpaper(cls, json_data = False) -> Union[Image.Image, dict]:
        """
        This function returns a movie wallpaper either in a Pil.Image.Image or dict format

        Parameters
        ----------
            :param json_data (bool, Optional) : If this is set to `True` the function will return the image 
                as a json/dict. If set to `False` it will return a `PIL.Image.Image` image

        Returns 
        -------
            Union[Image.Image, dict]: 
                If the param (json_data) is True it will return dict else PIL.Image.Image
                
        """
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