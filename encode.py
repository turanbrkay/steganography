import sys

from encryp_data import Encrypt
class Encode(Encrypt):
    def __init__(self, image_path, text):
        self.image_path = image_path
        self.text = text
    def embed_text(self):
        """
        Embeds the given text into the first 11 pixels of the image.

        The first 10 pixels indicate whether the image is encoded or not.
        The next 11 pixels represent the length of the text.

        :return: None
        """

        image = self.get_image(self.image_path)
        height,width, channels = image.shape

        binary_text = self.convert_ASCII_to_binary(self.text)
        length_of_text = format(len(binary_text), '011b')
        # append length of binary to beginning of binary_text
        new_binary = length_of_text + binary_text

        counter = 0
        for i, row in enumerate(image):
            for j, pixel in enumerate(row):
                # embed pixel's 0th element

                binary_string = self.convert_int_to_binary(pixel[0]) # 93 -> 101101011 (int to binary)

                if i == 0 and j < 10:
                    new_string = binary_string[:-1] + str(counter % 2)
                    counter += 1
                else:
                    new_string = binary_string[:-1] + new_binary[0]
                    new_binary = new_binary[1:]

                decimal_value = int(new_string, 2)  # convert changed number
                pixel[0] = decimal_value

                if(len(new_binary) == 0):
                    break
            if (len(new_binary) == 0):
                break



        self.save_embedded_image(image, "new_image")
        print("encoded.")

try:
    encode_obj = Encode(sys.argv[1], sys.argv[2])
    encode_obj.embed_text()
except ValueError as ve:
    print(f"Error: {ve}")
except TypeError as ty:
    print(f"Cannot handle grayscale image. You can try RGB color.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
