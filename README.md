# Steganography Tool

This simple steganography tool allows you to embed text messages into images.

## What is Steganography?

Steganography is a technique used to secretly transmit information. This technique makes the existence of embedded information understandable only to those who know a specific method. This tool enables you to embed a text message into an image and later extract that embedded message.

## How Does It Work?

This tool embeds a text message into an image by altering the least significant bit (LSB) of each pixel. The least significant bit is the binary digit at the end of the binary representation of each pixel's intensity value. By changing this bit, the tool can hide a message within the image without causing any noticeable changes to the naked eye.

## Usage

### Embedding

To perform the embedding process, you can use the following command:

```bash
python encode.py image.jpg "Hello, this is a secret message!"
```

In this command, the first argument specifies the image file, and the second argument represents the secret message that you want to hide within the image.
At the end of this command, a new image named 'new_image.png' will be created, and your text will be concealed within this image.

### Decoding

To perform the extraction process, use the following command:

```bash
python decode.py new_image.png
```

The command line takes one argument: the image from which the hidden message will be extracted.
