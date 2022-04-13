import requests
from io import BytesIO
from PIL import Image

def QRcode(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get('https://michaelapi.herokuapp.com/api/other/QRCode?Text={}'.format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)

def umdad(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get('https://michaelapi.herokuapp.com/Memes/um_dad?text={}'.format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)

def if_the_could_read(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get('https://michaelapi.herokuapp.com/Memes/if_the_could_read?text={}'.format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)


def I_wish(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get('https://michaelapi.herokuapp.com/filters/I_wish?text={}'.format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)