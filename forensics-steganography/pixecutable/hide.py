from PIL import Image
from math import log, sqrt

flag = list(zip(*[iter(open("main", "rb").read())]*3))

size = int(2**(log(sqrt(len(flag)-1))//log(2) + 1))

hidden = Image.new(mode="RGB", size=(size, size), color=(0x00, 0x00, 0x00))
pixels = hidden.load()

for pixel, code in zip(((j, i) for i in range(size) for j in range(size)), flag):
    hidden.putpixel(pixel, code)


hidden.save('./hidden.png')
