import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import random, string
import numpy as np

# ASCII_CHARS = ["@", "#", "＄", "%", "?", "*", "+", ";", ":", ",", "."]

# Contrast on a scale -10 -> 10
contrast = 10
density = ('$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|''()1{}[]?-_+~<>i!lI;:,"^`\'.')
density = density[:-11+contrast]
n = len(density)

def resize(image, new_width = 300):
    old_width, old_height = image.size
    new_height = round(new_width * (old_height // old_width) * 0.70)
    return image.resize((new_width, new_height))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    # pixels = image.getdata()
    ascii_str = "";
    # for pixel in pixels:
    #    ascii_str += ASCII_CHARS[pixel//25];
    # return ascii_str
    height = image.height
    width = image.width
    arr = np.array(image)
    for i in range(height):
        for j in range(width):
            p = arr[i,j]
            k = int(np.floor(p/256 * n))
            ascii_str += density[n-1-k]
            # print(density[n-1-k], end='')
    return ascii_str

# Now map the pixel brightness to the ASCII density glyphs.


def main():
    global image
    # Use absolute path!
    path = input("Enter the path to the image file : \n") 
    image = PIL.Image.open(path)
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image. ")
    # resize image
    image2 = resize(image);
    #convert image to greyscale image
    greyscale_image = to_greyscale(image2)
    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""
    # Split the string based on width of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
        
        
    # save the string to a plain text file
    rand_string = ''.join(random.choice(string.ascii_letters) for _ in range(5))
    fname = "ascii_image_" + rand_string + ".txt"
    with open(fname, "w") as f:
        f.write(ascii_img);
main()