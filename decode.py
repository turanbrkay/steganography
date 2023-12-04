from encryp_data import Encrypt
import sys
class Decode(Encrypt):
    def __init__(self,image_path):
        self.image_path = image_path

    def solve_puzzle(self):
        image = self.get_image(self.image_path)
        height, width, channels = image.shape

        number_of_letter = 0
        is_encoded = ''.join(self.convert_int_to_binary(image[0][j][0])[7] for j in range(10))

        if is_encoded != "0101010101":
            print("This image does not contain encrypted messages")
        else:
            length_of_text = ''.join(self.convert_int_to_binary(image[0][j][0])[7] for j in range(10, 21))
            length_of_text = int(length_of_text, 2)
            text = ""

            for row in range(height):
                for column in range(width):
                    if column < 21 and row == 0:
                        continue
                    text += self.convert_int_to_binary(image[row][column][0])[7]
                    length_of_text -= 1
                    if length_of_text == 0:
                        break

                if length_of_text == 0:
                    break

            print(f"Encrypted message: '{self.convert_binary_to_ASCII(text)}'")

decode_obj = Decode(sys.argv[1])
decode_obj.solve_puzzle()


