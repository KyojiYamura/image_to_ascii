from PIL import Image
import os

ASCII_CHARS = "@%#*+=-:."


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / float(width)
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def grayscale(image):
    return image.convert('L')


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str


def main(image_path):
    try:
        image = Image.open(image_path)
        image = resize_image(image)
        image = grayscale(image)
        ascii_str = pixels_to_ascii(image)
        output_folder = "saves"
        os.makedirs(output_folder, exist_ok=True)
        output_filename = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + ".txt")
        with open(output_filename, "w") as f:
            for i in range(0, len(ascii_str), image.width):
                f.write(ascii_str[i:i + image.width] + "\n")

        print(f"ASCII art saved to {output_filename}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    image_path = input("Enter the path to the PNG image: ")
    main(image_path)
