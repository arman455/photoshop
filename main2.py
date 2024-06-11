from PIL import Image
from PIL import ImageFilter

with Image.open('girl.jpg') as pic_original:
   pic_original.show()

   pic_gray = pic_original.convert('L')#Черно-белое изображение
   #pic_gray.save('girl1.jpg')
   pic_gray.show()

   pic_up = pic_gray.transpose(Image.ROTATE_90)#Развернутое изображение
   #pic_up.save('girl2.jpg')
   pic_up.show()

   pic_blur = pic_gray.filter(ImageFilter.BLUR)#Размытое изображение
   #pic_blur.save('girl3.jpg')
   pic_blur.show()