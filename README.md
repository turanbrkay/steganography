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
python steganography.py embed image.jpg "Hello, this is a secret message!"
