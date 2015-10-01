# ###################################################################
# dcutils.py - This module will contain the two main functions 
#			   for hiding and extracting the data
#
#	Crypto module installation
#	 simply run “python setup.py build” to build the package, 
#	 and “python setup.py install” to install it.
#
#	Example.
# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message = "The answer is no"
# ciphertext = obj.encrypt(message)

# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message2 = obj2.decrypt(ciphertext)
#
#	CFB, CBC, ECB
#
#
#
# ###################################################################
from Crypto import Random
from Crypto.Cipher import AES


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
	message = pad(message)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(key, AES.MODE_CFB, iv)
	print("Encrypted.")
	return iv + cipher.encrypt(message)

def decrypt(ciphertext, key):
	iv = ciphertext[:AES.block_size]
	cipher = AES.new(key, AES.MODE_CFB, iv)
	plaintext = cipher.decrypt(ciphertext[AES.block_size:])
	print("Decrypted.")
	return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):

	# ###################################################################
	#	open a file once with read only (binary) mode in byte format
	# ###################################################################
	# f = open(file_name, "rb")	
	# plaintext = bytearray(f.read())	#argument must be read-only pinned buffer, not bytearray
	

	# ###################################################################
	#	while file is opened, read only (binary)
	# ###################################################################
	with open(file_name, 'rb') as fo:
		plaintext = fo.read()
	# for bits in readFile:
	# 	print (bits)		# prints in RGBA value (A - Alpha, transparency)
	#print(plaintext)
	enc = encrypt(plaintext, key)
	with open(file_name + ".enc", 'wb') as fo:
		fo.write(enc)
	
def decrypt_file(file_name, key):
	with open(file_name, 'rb') as fo:
		ciphertext = fo.read()
	dec = decrypt(ciphertext, key)
	with open(file_name[:-4], 'wb') as fo:
		fo.write(dec)


# ###############################################################################################
# ENCRYPTION TESTING

# key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
# encrypt_file('images/stego_small.bmp', key)

# decrypt_file('images/stego_small.bmp', key)

def hide():

	return 0

def extract():

	return 0

