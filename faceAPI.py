from PIL import  ImageOps, Image
import numpy as np

im = Image.open("dataset/face-112.101.jpg")
col,row  = im.size
a = np.array(im)
print(a.shape,im.size)
print(a)
