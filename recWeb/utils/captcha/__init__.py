import random
import string
# Image：一个画布
# ImageDraw：一个画笔
# ImageFont:画笔的字体
from PIL import Image, ImageDraw, ImageFont


# Captcha验证码

class Captcha(object):
    # 生成几位数的验证码【类属性】
    number = 4
    # 验证码图片的宽度和高度【类属性】
    size = (100, 30)
    # 验证码字体大小【类属性】
    fontsize = 25
    # 加入干扰线的条数【类属性】
    line_number = 2

    # 构建一个验证码源文本
    SOURCE = list(string.ascii_letters)
    for index in range(0, 10):
        SOURCE.append(str(index))

    # 用来绘制干扰线
    @classmethod
    def __gene_line(cls, draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))  # 线的开始位置
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=cls.__gene_random_color(), width=2)  # width指线条宽度

    # 用来绘制干扰点
    @classmethod
    def __gene_points(cls, draw, point_chance, width, height):
        chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]
        for w in range(width):
            for h in range(height):
                tmp = random.randint(0, 100)
                if tmp > 100 - chance:
                    draw.point((w, h), fill=cls.__gene_random_color())

    # 生成随机的验证码图片背景颜色【start（颜色开始值）, end=255】
    @classmethod
    def __gene_random_color(cls, start=0, end=255):
        random.seed()  # 生成一个随机种子
        return (random.randint(start, end),
                random.randint(start, end), random.randint(start, end))

    # 随机选择一个字体
    @classmethod
    def __gene_random_font(cls):
        fonts = [
            'Courgette-Regular.ttf',
            'LHANDW.TTF',
            'Lobster-Regular.ttf',
            'verdana.ttf'
        ]
        font = random.choice(fonts)  # 在fonts列中随机选一个
        return 'utils/captcha/' + font

    # 用来随机生成一个字符串(包括英文和数字)
    @classmethod
    def gene_text(cls, number):
        # number是生成验证码的位数
        return ''.join(random.sample(cls.SOURCE, number))

    # 生成验证码【重点方法】（类方法可以通过Captcha.gene_graph_captcha直接使用）
    @classmethod
    def gene_graph_captcha(cls):
        # 验证码图片的宽和高
        width, height = cls.size
        # 创建图片   RGA【R：Red（红色）0-255、G：G（绿色）0-255、B：B（蓝色）0-255、A：Alpha（透明度）】
        image = Image.new('RGBA', (width, height), cls.__gene_random_color(0, 100))
        # 验证码的字体【字体类型、字体大小】
        font = ImageFont.truetype(cls.__gene_random_font(), cls.fontsize)
        # 创建画笔【指定在image上画东西】
        draw = ImageDraw.Draw(image)
        # 生成字符串
        text = cls.gene_text(cls.number)
        # 获取字体的尺寸
        font_width, font_height = font.getsize(text)
        # 填充字符串【x坐标y坐标、text、font、字体颜色】
        draw.text(((width - font_width) / 2, (height - font_height) / 2), text, font=font,
                  fill=cls.__gene_random_color(150, 255))
        # 绘制干扰线【增加机器识别的难度】
        for x in range(0, cls.line_number):
            cls.__gene_line(draw, width, height)
        # 绘制噪点
        cls.__gene_points(draw, 10, width, height)

        # with open('captcha.png', 'wb') as fp:
        #     image.save(fp)

        return (text, image)  # 返回验证码的文本信息和图片
