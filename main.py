from PIL import Image
import numpy as np
import binascii


def convert_grayscale(image_path):
    """Convert image to grayscale and save."""
    image = Image.open(image_path, "r").convert('L')
    image.save(image_path)


def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")

    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = np.array(pixel_values).reshape((width, height, channels))
    return pixel_values


def convert_int_to_binary(value):
    binary_string = '{0:08b}'.format(value)
    return binary_string

def convert_ASCII_to_binary(text):
    byte_array = text.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)
    return binary_string


def convert_binary_to_ASCII(text):
    binary_int = int(text, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    # Create the byte array and strip leading zeros
    binary_array = binary_int.to_bytes(byte_number, "big").lstrip(b'\x00')
    ascii_text = binary_array.decode()
    return ascii_text


def process(image_path, text):
    image = get_image(image_path)
    width, height, channels = image.shape

    print(image[0])
    print("-"*50)


    binary_text = convert_ASCII_to_binary(text)
    len_text = format(len(binary_text), '011b')
    # append length of binary to beginning of binary_text
    new_binary = len_text + binary_text



    for i in range((len(new_binary)/width)+1):
        for j in range(5):
            binary_string = convert_int_to_binary(image[i][j][0])
            print(binary_string)
            new_string = binary_string[:-1] + "X"



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    string = "Torres"
    string2 = "0b10001100110010101110010011011100110000101101110011001000110111100100000010101000110111101110010011100100110010101110011"
    process("small.jpg", "Fernando Torres")

