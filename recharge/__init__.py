# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  Initialize the package

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""

from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.


VERSION = (0, 0, 1, 'beta')


def get_version():
    """
    Returns the version as a human-format string.
    """
    ver = '.'.join([str(i) for i in VERSION[:-1]])
    if VERSION[-1]:
        ver = '%s-%s' % (ver, VERSION[-1])
    return ver