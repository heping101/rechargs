# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  Initialize the package

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""

from os import path

# --------------------------------------
# My Predefined
# --------------------------------------

# 自定义：项目根路径作为系统起始目录
D_APP_ROOT = path.realpath(path.join(path.dirname(__file__), '../..'))

# --------------------------------------
# CORE
# --------------------------------------

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'runfast',
        'USER': 'runfast',
        'PASSWORD': 'runfast',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    },
    'OPTIONS': {'charset': 'utf8', 'init_command': 'SET storage_engine=InnoDB'},
}
