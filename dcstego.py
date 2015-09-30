# dcstego.py

import argparse

def main():

	exit(0)

if __name__ == '__main__':
	parser = argparse.ArgumentParser() 
	parser.add_argument("image", help="Image to use for overlay")
    parser.add_argument("text", help="Text to display")
    parser.add_argument("fontsize", type=int, help="Font size")
    parser.add_argument("-f", "--font", help="Font to use. Default=\"Impact.ttf\"")
    parser.add_argument("-x", "--xpos", type=int, help="X position to place text. Defaults to center of image.")
    parser.add_argument("-y", "--ypos", type=int, help="Y position to place text. Defaults to center of image.")
    
	args = parser.parse_args()
	main(args)