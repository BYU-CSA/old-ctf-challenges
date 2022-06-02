from PIL import Image


hidden = Image.open('./hidden.png').convert()
size = hidden.size[0]
pixels = hidden.load()

flag = (color for j in range(size) for i in range(size) for color in hidden.getpixel((i,j)))

open("other", "wb").write(bytes(flag))