import requests
from io import BytesIO
from PIL import Image


def MctextMaker(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get('https://michaelapi.herokuapp.com/api/text/Minecraft?Text={}'.format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)

def Pokemontextmaker(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get("https://michaelapi.herokuapp.com/api/text/pokemon?Text={}" .format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)

def theavengerstextmaker(text) -> Image.Image:
    message = text.replace(" ", "%20")
    response = requests.get("https://michaelapi.herokuapp.com/api/text/theavengers?Text={}" .format(message))
    image_data = BytesIO(response.content)
    image_data.seek(0)
    image = Image.open(image_data)
    return(image)