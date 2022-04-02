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