# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  Initialize the package

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xxxx',
        'USER': 'xxxx',
        'PASSWORD': 'xxxx',
        'HOST': 'xxxx',
        'PORT': '3306',
    },
    'OPTIONS': {'charset': 'utf8', 'init_command': 'SET storage_engine=InnoDB'},
}

