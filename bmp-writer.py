"""A module for dealing with BMP bitmap image files"""



def _int32_to_bytes(i):
    """Convert an integer in bytes."""
    return bytes((i & 0xff, i >> 8 & 0xff, i >> 16 & 0xff, i >> 24 & 0xff))

def write_grayscale(filename, pixels):
	"""Creates and writes grayscale BMP file.

	Args: 
		filename: The name of the BMP file to be created.

		pixels: A rectangular image stored as a sequence of rows. Each row must be an iterable series of integers in the range 0-255.

	Raises:
		ValueError: If any of the integer values are out of range.
		OSError: If the file could not be written.
	"""

	height = len(pixels)
	width = len(pixels[0])

	with open(filename, 'wb') as bmp:
		#BMP header
		bmp.write(b'BM')

		size_bookmark = bmp.tell() 
		bmp.write(b'\x00\x00\x00\x00')

		bmp.write(b'\x00\x00')
		bmp.write(b'\x00\x00')

		pixel_offset_bookmark = bmp.tell()
		bmp.write(b'\x00\x00\x00\x00')

		#Image header
		bmp.write(b'\x28\x00\x00\x00')
		bmp.write(_int32_to_bytes(width))
		bmp.write(_int32_to_bytes(height))
		bmp.write(b'\x01\x00')
		bmp.write(b'\x08\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')

		#Color palette - a linear grayscale
		for c in range(256):
			bmp.write(bytes((c,c,c,0)))

		#Pixel data
		pixel_data_bookmark = bmp.tell()
		for row in reversed(pixels):#BMP file are bottom to top
			row_data = bytes(row)
			bmp.write(row_data)
			padding = b'\x00' * ((4 - (len(row) % 4)) % 4)
			bmp.write(padding)

		#End of file
		eof_bookmark = bmp.tell()

		#Fill in file size placeholder
		bmp.seek(size_bookmark)
		bmp.write(_int32_to_bytes(eof_bookmark))

		#Fill in pixel offset placeholder
		bmp.seek(pixel_offset_bookmark)
		bmp.write(_int32_to_bytes(eof_bookmark))