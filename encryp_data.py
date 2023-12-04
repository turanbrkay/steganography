import numpy as np
from PIL import Image
class Encrypt(object):
    def __init__(self, image_path, text):
        self.image_path = image_path
        self.text = text

    def convert_grayscale(self,Image,image_path):
        """Convert image to grayscale and save."""
        image = Image.open(image_path, "r").convert('L')
        image.save(image_path)

    def get_image(self,image_path):
        """Get a numpy array of an image so that one can access values[x][y]."""
        image = Image.open(image_path, "r")
        width, height = image.size
        pixel_values = list(image.getdata())
        if image.mode == "RGB":
            channels = 3
        elif image.mode == "RGBA":
            channels = 4
        elif image.mode == "L":
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
            return None

        pixel_values = np.array(pixel_values).reshape((height, width, channels))
        return pixel_values

    def convert_int_to_binary(self, value):
        binary_string = '{0:08b}'.format(value)
        return binary_string

    def convert_ASCII_to_binary(self,text):
        byte_array = text.encode()
        binary_int = int.from_bytes(byte_array, "big")
        # python added 0b for represent binary string but we removed it.
        binary_string = bin(binary_int)[2:]
        return binary_string

    def convert_binary_to_ASCII(self,text):
        binary_int = int(text, 2)
        byte_number = binary_int.bit_length() + 7 // 8
        # Create the byte array and strip leading zeros
        binary_array = binary_int.to_bytes(byte_number, "big").lstrip(b'\x00')
        ascii_text = binary_array.decode()
        return ascii_text

    def save_embedded_image(self, image, image_path):
        new_image = Image.fromarray(image.astype(np.uint8))
        new_image.save(image_path + ".png")


