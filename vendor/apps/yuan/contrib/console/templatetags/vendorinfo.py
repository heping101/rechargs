# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  Configuration vars which dump to templates

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.template import Library
import yuan

register = Library()


def vendor_version():
    """
    Returns the yuan's version
    """
    return yuan.get_version()

register.simple_tag(vendor_version)
