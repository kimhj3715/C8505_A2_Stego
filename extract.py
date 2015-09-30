#extract
from PIL import Image, ImageDraw, ImageMath

stegged=Image.open("merged.bmp")
red, green, blue = stegged.split()
watermark=ImageMath.eval("(a&0x1)*255",a=red) # convert to 0 or 255
watermark=watermark.convert("L")
watermark.save("extracted-watermark.bmp")