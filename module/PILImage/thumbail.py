# from PIL import Image, ImageFilter

'生成缩略图'

# im = Image.open("test.png")
# print(im.format, im.size, im.mode)
# # PNG(400,300) RGB
# im.thumbnail((200, 100))
# im.save("thumb.jpg", "JPEG")

'模糊图片'
# im = Image.open('test.png')
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'JPEG')

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


#随机字母
def rndChar():
    return chr(random.randint(65, 90))


#随机颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))


def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


width = 64 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
#创建Font对象
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)
draw = ImageDraw.Draw(image)
#填充元素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

#输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'JPEG')
