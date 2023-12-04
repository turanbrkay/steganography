# Steganography Tool

This simple steganography tool allows you to embed text messages into images.

## What is Steganography?

Steganography is a technique used to secretly transmit information. This technique makes the existence of embedded information understandable only to those who know a specific method. This tool enables you to embed a text message into an image and later extract that embedded message.

## How Does It Work?

This tool embeds a text message into an image by altering specific pixels and then allows you to extract that message using the same program. The first 10 pixels indicate whether the image contains an encrypted message. The next 11 pixels specify the length of the embedded text.

## Usage

### Embedding

To perform the embedding process, you can use the following command:

```bash
python steganography.py embed image.jpg "Hello, this is a secret message!"
