#Python Image Library
from PIL import Image

with Image.open("owl.jpg") as photo:
    print("size:", photo.size)
    print("format:", photo.format)
    print("mode:", photo.mode)
    #print(photo.info)
    photo.show()
    #photo.save("owl2.jpg")