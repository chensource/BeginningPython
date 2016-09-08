from PIL import Image, ImageDraw, ImageFont


def add_num(picPath, num):
    image = Image.open(picPath)
    x, y = image.size
    myfont = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', x // 5)
    ImageDraw.Draw(image).text((2 * x / 3, 0),
                               str(num),
                               font=myfont,
                               fill='red')
    image.save('1234.jpg')


if __name__ == '__main__':
    add_num('123.jpg', 10)
