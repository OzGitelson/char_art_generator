from PIL import Image, ImageOps

def grayscale(image):
    return ImageOps.grayscale(image)

def resize (image, new_w):
    w, h=image.size
    new_h=(new_w/w)*h
    return image.resize((int(new_w), int(new_h)))

def to_ascii(path, width):
    CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

    image = Image.open(path)
    image= grayscale(image)
    image=resize(image, width)
    # image.show()
    pix=image.getdata()
    char_string=''
    w, h=image.size
    for n, p in enumerate(pix):
        char_string+=CHARS[p//25]
        if n%w==0 and n!=0:
            char_string+='\n'

    outfile=open('output.txt', 'w')
    outfile.write(char_string)
    outfile.close()



to_ascii('download.jpg', 150)