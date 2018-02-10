import os
from PIL import Image

iPhone5_WIDTH = 1136
iPhone5_HEIGHT = 640


def change_image_width_hieght(file_path):
    L = [x for x in os.listdir('.')
         if os.path.isfile(x) and os.path.splitext(x)[1] == '.jpg']
    # print(len(L))
    i = 1
    for img in L:
        # print(img)
        image = Image.open(img)

        w, h = image.size
        w = iPhone5_WIDTH
        h = iPhone5_HEIGHT
        # print(image)
        # name = os.path.join(path, img)

        image.resize((w, h), Image.ANTIALIAS)
        image.save('iPhone5_' + str(i) + '.jpg')
        i += 1


if __name__ == '__main__':
    change_image_width_hieght('\\')
