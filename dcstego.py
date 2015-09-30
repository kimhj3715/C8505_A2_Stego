# ###################################################################
# dcstego.py - the main function that will contain the general functionality
#			   such as parsing command line arguments, checking file sizes,
#			   etc
#
#
#
#
# ###################################################################

# from gimpfu import *
from PIL import Image, ImageDraw, ImageMath
import argparse
import dcutils		# usage: dcutils.method_name() || dcutils.variable_name
import dcimage

# Opens an image at the given path
def open_image(path, mode):
    image = None
    try:
        image = Image.open(path)
    except Exception as e:
        print("Image not found")
        print(e)
        return
    return image

def check_size(cImg, sImg):  

	return 0


def main(args):
	coverImg = open_image(args.cover_image, "rb")	# read only in binary
	secretImg = open_image(args.secret_image, "rb") 
	
	# check the size, for now just make secret image size equals cover image
	secretImg = secretImg.resize(coverImg.size)


	red, green, blue = coverImg.split()
	sred, sgreen, sblue = secretImg.split()




	red2 = ImageMath.eval("convert(a&0xFE|b&0x1,'L')", a=red, b=sred)
	green2 = ImageMath.eval("convert(a&0xFE|b&0x1,'L')", a=green, b=sgreen)
	blue2 = ImageMath.eval("convert(a&0xFE|b&0x1,'L')", a=blue, b=sblue)


	out = Image.merge("RGB", (red2, green2, blue2))
	out.save("merged.bmp")












	exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("cover_image", help="Image includes secret image")
    parser.add_argument("secret_image", help="Image that hides in cover image")
    #parser.add_argument("output file", help="Final image")
    args = parser.parse_args()

    main(args)