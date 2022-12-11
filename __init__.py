import sys
import numpy as np
import math
import os

from PIL import Image

# 10 levels of gray
gscale = "@%#*+=-:. "

#return average grayscale valueof given image or image tile
def getAverageL(image):

    #Turn image into a 3d array where im = [pixelRow, pixelColumn, colorChannel]
    im = np.array(image)

    #Get image width and height
    width, height = im.shape

    #Get average brightness value of image/tile
    return np.average(im.reshape(width*height))
    

#Convert passed image into a string counterpart with each pixel represented by an ASCII character
def convertImageToAscii(imageFilePath):

    #convert image to grayscale as well as open image
    image = Image.open(imageFilePath).convert("L")

    #Get width and height of image
    W, H = image.size[0], image.size[1]

    #Initialize ascii image string variable
    asciiImage = []

    print("Image Size: ", W, "*", H)
    print()
    print("...Generating ASCII Image...")

    #Determine how many pixels to convert to ASCII characters
    pixelAmount = W*H

    #Define how many pixels are converted to ASCII characters
    asciiCount = 0;

    #Define percentage of completed pixels
    asciiPerc = 0;

    print("Converted:",asciiPerc, "%")
    
    #Generate dimensions list
    #Iterate through each row of image
    for j in range(H-1):
        
        #Append empty string
        asciiImage.append("")

        #Iterate through each image column
        for i in range(W-1):

            #Crop current image pixel which. loops will iterate through each image pixel
            croppedImage = image.crop((i, j, (i + 1), (j + 1)))

            #Get pixel average RGB value which correstponds to it's average brightness
            avg = int(getAverageL(croppedImage))

            #Get ASCII shading value corresponding to current pixel brightness
            #If pixel brightness is high, then a character such as @ is assigned, if low, no character
            gsval = gscale[int((avg*(len(gscale)-1))/255)]

            #Append ascii character correponding to pixel to asciiImage array
            asciiImage[j] += gsval
            asciiCount += 1

        #Begin a new row for image
        asciiImage[j] += "\n"

        #Determine percentage of converted characters. If percentage changes by 1%, then print out converted
        #percentage
        prevPerc = asciiPerc
        asciiPerc = int((asciiCount/pixelAmount)*100)
        if(asciiPerc != prevPerc):
            print("Converted: ",asciiPerc, "%")
        
        asciiImageString = "".join(str(i) for i in asciiImage)

    print("100% Converted!")
    print("Done")


    #Finally, return completed ascii image string
    return asciiImageString


def sayDaTruth():
    print("OMAR MAAOUANE IS THE AWESOMEST HUMAN BEING TO EVER LIVE!!!")