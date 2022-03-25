import requests
from io import BytesIO
from PIL import Image

def teaimage() -> Image.Image:
    response = requests.get('https://micswallpaperapi.herokuapp.com/wallpaper')
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)