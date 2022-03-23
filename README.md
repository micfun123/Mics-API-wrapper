# Mics-API-wrapper

This is a package to simplify the use of my APIs. The wrapper will make doing all of the most common tasks of the API simple as well as fast. This prevents you having to use requests and think about how you get the files.

## Example Usage: 
```py

#Using the json forms

imageurl = Wallpapersimagelink()
print(imageurl)

imageurl = filmimagelink()
print(imageurl)

#using images 
# wallpapersimage , moviewallpaperimage
#Example on saving the photo. 

from PIL import Image 
import PIL 

# creating a image object (main image) 
im1 = Image.open(wallpapersimage()) 
  
# save a image using extension
im1 = im1.save("Test.jpg")


from PIL import Image 
import PIL 

# creating a image object (main image) 
im1 = Image.open(moviewallpaperimage()) 
  
# save a image using extension
im1 = im1.save("Test.jpg")

```


# API List

https://hotbeverage.herokuapp.com/docs   = Has photos and soon info on hot drinks<br>
https://michaelstextapi.herokuapp.com/docs  =  Will turn text in the a image with the sytle of a games title font<br>
https://micswallpaperapi.herokuapp.com/docs  =  A large collection of wall papers 