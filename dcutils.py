# ###################################################################
# dcutils.py - This module will contain the two main functions 
#			   for hiding and extracting the data
#
#
# ###################################################################
from Crypto import Random
from Crypto.Cipher import AES

obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)

obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message2 = obj2.decrypt(ciphertext)


print(ciphertext)
print(message2)



def encrypt_file(file_name):

	# ###################################################################
	#	while file is opened, read only (binary)
	# ###################################################################
	# with open('images/stego_small.bmp', 'rb') as fo:
	# 	b = bytes(fo.read())
	# print(b)


	# ###################################################################
	#	open a file once and read only (binary) in byte format
	# ###################################################################
	f = open(file_name, "rb")	
	readFile = bytearray(f.read())
	# for bits in readFile:
	# 	print (bits)		# prints in RGBA value (A - Alpha, transparency)
	print(readFile)
	






	return 0

def decrypt_file():

	return 0

def hide():

	return 0

def extract():

	return 0


encrypt_file('images/stego_small.bmp')