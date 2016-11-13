# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  Initialize the package

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import os

D_YUAN_ROOT = os.path.realpath(os.path.dirname(__file__))

VERSION = (0, 1, 0, 'beta')


def get_version():
    """
    Returns the version as a human-format string.
    """
    ver = '.'.join([str(i) for i in VERSION[:-1]])
    if VERSION[-1]:
        ver = '%s-%s' % (ver, VERSION[-1])
    return ver
