# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  验证码相关的工具函数.

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from os import path
import random
import math
from cStringIO import StringIO
from PIL import Image, ImageFont, ImageDraw

from django.http import HttpResponse
from django.conf import settings

from yuan import D_YUAN_ROOT

AUTHENTICATION_CANVAS = getattr(settings, 'AUTHENTICATION_CANVAS', path.join(D_YUAN_ROOT, 'assets/noisy.png'))
AUTHENTICATION_TTFONT = getattr(settings, 'AUTHENTICATION_TTFONT', path.join(D_YUAN_ROOT, 'assets/noisy.ttf'))
AUTHENTICATION_FORMAT = getattr(settings, 'AUTHENTICATION_FORMAT', 'image/png')


def new_authentication_code(request, length=5):
    """ 生成随机字符串 """
    char_list = 'ABCDEFGHJKLMNPQRSTVWXYZ'
    auth_code = ''
    for i in range(0, length):
        auth_code += random.choice(char_list)
    request.session['AUTHENTICATIONCODE'] = auth_code


def dump_authentication_code(request):
    """ 将随机字符串显示为验证码图片 """
    auth_code = request.session.get('AUTHENTICATIONCODE', '00000')
    colorlist = ['#ca56ce', '#2255bb', '#bd4126', '#794adc', '#c5182e', '#44493d', '#1c8a12', '#963421']

    # load the font file
    img_font = ImageFont.truetype(AUTHENTICATION_TTFONT, 26)
    img_file = Image.open(AUTHENTICATION_CANVAS)

    img_buff = Image.new('RGBA', img_file.size)
    img_draw = ImageDraw.Draw(img_buff)
    ijiggle = 5
    fillcolor = random.choice(colorlist)
    for i, vchar in enumerate(auth_code):
        img_draw.text((3 + i * 25 + random.randint(1, ijiggle), 3 + random.randint(1, ijiggle)), vchar, font=img_font, fill=fillcolor)
    del img_draw

    # transform the image
    resolution = 10
    x_points = img_buff.size[0] / resolution + 2
    y_points = img_buff.size[1] / resolution + 2
    x_rows = []
    y_rows = []
    l_func = get_transform(img_buff)
    for j in xrange(y_points):
        x_row = []
        y_row = []
        for i in xrange(x_points):
            trans_x, trans_y = l_func(i * resolution, j * resolution)
            # Clamp the edges so we don't get black undefined areas
            trans_x = max(0, min(img_buff.size[0] - 1, trans_x))
            trans_y = max(0, min(img_buff.size[1] - 1, trans_y))
            x_row.append(trans_x)
            y_row.append(trans_y)
        x_rows.append(x_row)
        y_rows.append(y_row)

    # Create the mesh list, with a transformation for
    # each square between points on the grid
    mesh = []
    for j in xrange(y_points - 1):
        for i in xrange(x_points - 1):
            mesh.append((
                # Destination rectangle
                (i * resolution, j * resolution,
                 (i + 1) * resolution, (j + 1) * resolution),
                # Source quadrilateral
                (x_rows[j][i], y_rows[j][i],
                 x_rows[j + 1][i], y_rows[j + 1][i],
                 x_rows[j + 1][i + 1], y_rows[j + 1][i + 1],
                 x_rows[j][i + 1], y_rows[j][i + 1])
            ))

    img_buff = img_buff.transform(img_buff.size, Image.MESH, mesh, Image.BILINEAR)

    img_file.paste(img_buff, None, img_buff)

    # dump image data
    img_buffer = StringIO()
    img_file.save(img_buffer, 'PNG')

    return HttpResponse(img_buffer.getvalue(), content_type=AUTHENTICATION_FORMAT)


def check_authentication_code(request, vcode):
    """ 检查给定的验证码是否与session中存储的相同 """
    isok = False
    if vcode:
        isok = (request.session.get('AUTHENTICATIONCODE', None) == vcode.upper())
    return isok


def get_transform(image):
    """Return a transformation function, subclasses should override this"""
    amplitude_range = (3, 6.5)
    period_range = (0.04, 0.1)
    amplitude = random.uniform(*amplitude_range)
    period = random.uniform(*period_range)
    offset = (random.uniform(0, math.pi * 2 / period),
              random.uniform(0, math.pi * 2 / period))

    return (
        lambda x, y, a=amplitude, p=period, o=offset:
        (math.sin((y + o[0]) * p) * a + x,
         math.sin((x + o[1]) * p) * a + y))
