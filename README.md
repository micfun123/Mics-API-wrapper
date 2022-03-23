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
```


```py
# Example of how to use the Wallpaper class
from MicsAPIwrapper import Wallpaper

# Image
image1 = Wallpaper.movie_wallpaper()
image1.save("movie_wallpaper.png")

# Json version
json_movie_wallpaper = Wallpaper.movie_wallpaper(json_data=True)
print(json_movie_wallpaper)

# Image
image2 =  Wallpaper.wallpaper()
image2.save("wallpaper.png")

# Json version
json_wallpaper = Wallpaper.wallpaper(json_data=True)
print(json_wallpaper)
```


# API List

https://hotbeverage.herokuapp.com/docs   = Has photos and soon info on hot drinks (not started) <br>
https://michaelstextapi.herokuapp.com/docs  =  Will turn text in the a image with the sytle of a games title font (working on adding to wrapper)<br>
https://micswallpaperapi.herokuapp.com/docs  =  A large collection of wall papers (Added)
