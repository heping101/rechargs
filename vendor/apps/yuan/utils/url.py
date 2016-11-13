# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  HTTP相关的工具函数

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import hashlib

from django.utils.encoding import smart_unicode, DjangoUnicodeDecodeError


def asset_authenticated_key(request, keyname, keypass):
    """
    根据客户端的某些信息和指定的Pass，生成一个MD5串，用于静态附件的限制访问key
    """
    remote_addr = absolute_unicode(request.META.get('REMOTE_ADDR', u''))
    user_agent = absolute_unicode(request.META.get('HTTP_USER_AGENT', u''))
    if remote_addr and user_agent:
        key = hashlib.md5((u'%s%s%s' % (keypass, remote_addr, user_agent)).encode('utf-8')).hexdigest()
        return u'?%s=%s' % (keyname, key)
    else:
        return u'?%s=' % (keyname, )


def absolute_unicode(str_sub, failure_charset='GB18030'):
    """
    将UTF-8或者GB中文编码转换为Unicode
    """
    # 对于已经是unicode了，直接返回
    if isinstance(str_sub, unicode):
        return str_sub

    str_return = u''
    try:
        # 先试试Django的转码工具
        str_return = smart_unicode(str_sub)
    except DjangoUnicodeDecodeError:
        # 非UTF-8编码，我们试试中文编码
        try:
            str_return = unicode(str_sub, failure_charset, 'ignore')
        except UnicodeDecodeError:
            # 其他编码？出错再说
            str_return = str_sub
    return str_return
