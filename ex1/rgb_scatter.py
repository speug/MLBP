import os
import matplotlib.pyplot as plt
from PIL import Image

files = os.listdir("materials/Webcam/")
rs = []
gs = []
for f in files:
    im = Image.open("materials/Webcam/" + f)
    pixs = im.load()
    s = im.size
    r = 0
    g = 0
    for x in range(0,s[0]):
        for y in range(0,s[1]):
            pix = pixs[x,y]
            r = r + pix[0]
            g = g + pix[1]
    rs.append(r)
    gs.append(g)
plt.scatter(rs,gs)
plt.ylabel("Sum of greens")
plt.xlabel("Sum of reds")
plt.show()
