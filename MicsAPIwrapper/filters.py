import requests
from io import BytesIO
from PIL import Image

def trash(url) -> Image.Image:
    response = requests.get('https://michaelapi.herokuapp.com/filters/trash?image_url={}'.format(url))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)

def wanted(url) -> Image.Image:
    response = requests.get('https://michaelapi.herokuapp.com/filters/wanted?image_url={}'.format(url))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)