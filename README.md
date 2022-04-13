# Mics-API-wrapper

This is a package to simplify the use of my APIs. The wrapper will make doing all of the most common tasks of the API simple as well as fast. This prevents you having to use requests and think about how you get the files.

# Install 
```py
pip install Mics-API-Wrapper
```

## Example Usage: 
```py
from MicsAPIwrapper import Wallpapersimagelink , filmimagelink
#Using the json forms

imageurl = Wallpapersimagelink()
print(imageurl)

imageurl = filmimagelink()
print(imageurl)

#using images 
# wallpapersimage , moviewallpaperimage
#Example on saving the photo. 
from MicsAPIwrapper import wallpapersimage ,moviewallpaperimage

from PIL import Image 
import PIL 
# save a image using extension
wallpapersimage().save("Test.jpg")

from PIL import Image 
import PIL 
# save a image using extension
moviewallpaperimage().save("Test.jpg")

#Text 
# creating a image object (main image) 
MctextMaker("Cake is a Lie").save("Test.jpg")
  
#pokemon ones
Pokemontextmaker("Cake is a Lie").save("Test.jpg")

#theavengerstextmaker
theavengerstextmaker("Cake is a Lie").save("Test.jpg")

#drinks
#tea coffee

from MicsAPIwrapper import teaimage, coffeeimage

from PIL import Image 
import PIL 
# save a image using extension
teaimage().save("Test.jpg")

coffeeimage().save("Test.jpg")


#memes

umdad("Cake is a Lie").save("Test.jpg")

if_the_could_read("Cake is a Lie").save("Test.jpg")

I_wish("Cake is a Lie").save("Test.jpg")

#image filter

trash("https://images-ext-2.discordapp.net/external/XBD-gTDJR8JwlJbdDNsekNPIhoJkYeHiwbFf2iOJOyA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/481377376475938826/8d0e7151738e8dd25cc6f417a430e669.png").save("Test.jpg")

wanted("https://images-ext-2.discordapp.net/external/XBD-gTDJR8JwlJbdDNsekNPIhoJkYeHiwbFf2iOJOyA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/481377376475938826/8d0e7151738e8dd25cc6f417a430e669.png").save("Test.jpg")

```




# API List

https://hotbeverage.herokuapp.com/docs   = Has photos and soon info on hot drinks <br>
https://michaelstextapi.herokuapp.com/docs  =  Will turn text in the a image with the sytle of a games title font (working on adding to wrapper)<br>
https://micswallpaperapi.herokuapp.com/docs  =  A large collection of wall papers (Added)
