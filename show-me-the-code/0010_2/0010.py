from PIL import Image, ImageDraw, ImageFont
import string
import random


def get_generate_authenticode():
    # 获取随机数
    letters = ''.join([random.choice(string.ascii_letters) for i in range(4)])
    # 绘制图片
    width = 100
    height = 40
    im = Image.new('RGB', (width, height), (255, 255, 255))

    #文字画图
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', width // 5)

    for i in range(4):
        dr.text((5 + i * 20, 5), letters[i], (random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255)), font)

    del dr

    # 改变背景
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(
                    0, 255), random.randint(0, 255)))

    # 保存图片
    im.save('t1.png')


if __name__ == '__main__':
    get_generate_authenticode()
