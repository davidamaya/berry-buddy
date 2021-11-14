from tkinter import *
import requests
from io import BytesIO
from PIL import Image
from urllib import request as req

def createMap(filename_wo_extension, center=None, zoom=None, imgsize="500x500", imgformat="jpeg", maptype="satellite", markers=None):
    # need to get lat/long from db (currently text files)
    # also need berry name for marker Name
    request = "http://maps.google.com/maps/api/staticmap?"
    if center != None:
        request += "center=%s&" % center
    if center != None:
        request += "zoom=%i&" % zoom
    request += "size=%ix%i&" % (imgsize)  # tuple of ints, up to 640 by 640
    request += "format=%s&" % imgformat
    request += "maptype=%s&" % maptype
    if markers != None:
        for marker in markers:
                request += "%s&" % marker
    request += "sensor=false&"   # must be given, deals with getting loction from mobile device
    request += "key=AIzaSyCz2WexsSRoX06wi7nkEqT1omuoWN4Pji4&"
    response = requests.get(request)
    Image.open(BytesIO(response.content)).convert('RGB').save(filename_wo_extension + "." + imgformat)
