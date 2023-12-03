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
    print(image.size)
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None

    pixel_values = np.array(pixel_values).reshape((height,width , channels))
    return pixel_values


def convert_int_to_binary(value):
    binary_string = '{0:08b}'.format(value)
    return binary_string

def convert_ASCII_to_binary(text):
    byte_array = text.encode()
    binary_int = int.from_bytes(byte_array, "big")
    # python added 0b for represent binary string but we removed it.
    binary_string = bin(binary_int)[2:]
    return binary_string


def convert_binary_to_ASCII(text):
    binary_int = int(text, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    # Create the byte array and strip leading zeros
    binary_array = binary_int.to_bytes(byte_number, "big").lstrip(b'\x00')
    ascii_text = binary_array.decode()
    return ascii_text

def save_embedded_image(image,image_path):
    new_image = Image.fromarray(image.astype(np.uint8))
    new_image.save(image_path+".png")

def embed_text(image_path, text):
    image = get_image(image_path)
    height,width, channels = image.shape

    binary_text = convert_ASCII_to_binary(text)

    length_of_text = format(len(binary_text), '011b')
    # append length of binary to beginning of binary_text
    new_binary = length_of_text + binary_text
    print("Number of turn height: " ,int(len(new_binary)/width)+1)

    for i, row in enumerate(image):
        for j, pixel in enumerate(row):
            # embed pixel's 0th element
            binary_string = convert_int_to_binary(pixel[0]) # 93 -> 101101011 (int to binary)
            new_string = binary_string[:-1] + new_binary[0]
            decimal_value = int(new_string, 2) #convert changed number
            pixel[0] = 255 #embed
            pixel[1] = 0  # embed
            pixel[2] = 0  # embed
            new_binary = new_binary[1:]

            if(len(new_binary) == 0):
                break
        if (len(new_binary) == 0):
            break




    print("-" * 40)
    print(image[0])
    print(len(image[0]))
    save_embedded_image(image, "new_image")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    string = "Torres"
    string2 = "0b10001100110010101110010011011100110000101101110011001000110111100100000010101000110111101110010011100100110010101110011"
    embed_text("small.jpg", "Fernando Torres")

