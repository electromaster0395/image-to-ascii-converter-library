from __init__ import *

asciiImageString = convertImageToAscii("testImages/me.jpg")
f = open("outTest.txt", "w")
f.write(asciiImageString)
f.close()
