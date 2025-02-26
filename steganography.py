from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_data(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = text_to_binary(secret_message) + '1111111111111110'  # Delimiter to indicate end of message
    
    pixels = list(image.getdata())
    new_pixels = []

    binary_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify RGB channels
            if binary_index < len(binary_message):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_path)
    print(f"Data hidden successfully in {output_path}")

# Example usage
hide_data("test_image.png", "Secret Message", "encoded_image.png")


from PIL import Image

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def hide_data(image_path, secret_message, output_path):
    image = Image.open(image_path)
    binary_message = text_to_binary(secret_message) + '1111111111111110'  # Delimiter to indicate end of message
    
    pixels = list(image.getdata())
    new_pixels = []

    binary_index = 0
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):  # Modify RGB channels
            if binary_index < len(binary_message):
                new_pixel[i] = new_pixel[i] & ~1 | int(binary_message[binary_index])
                binary_index += 1
        new_pixels.append(tuple(new_pixel))

    image.putdata(new_pixels)
    image.save(output_path)
    print(f"Data hidden successfully in {output_path}")

# Example usage
hide_data("test_image.png", "Secret Message", "encoded_image.png")


def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(char, 2)) for char in chars if int(char, 2) != 254)

def extract_data(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_data = ''
    for pixel in pixels:
        for i in range(3):  
            binary_data += str(pixel[i] & 1)
    
    delimiter = '1111111111111110'
    if delimiter in binary_data:
        binary_data = binary_data[:binary_data.index(delimiter)]
    
    secret_message = binary_to_text(binary_data)
    print("This is Himanshu Kardam", secret_message)

# Example usage
extract_data("encoded_image.png")
