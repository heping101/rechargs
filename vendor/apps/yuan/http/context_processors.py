# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  context processor

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.conf import settings


def siteinfo(request):
    """
    settings site info
    """
    return {
        'STATIC_URL'        : getattr(settings, 'STATIC_URL', '/assets/'),
        'MEDIA_URL'         : getattr(settings, 'MEDIA_URL', '/static/'),
        'LANGUAGE_CODE'     : getattr(settings, 'LANGUAGE_CODE', 'zh-cn'),
        'SITEINFO_NAME'     : getattr(settings, 'SITEINFO_NAME', 'dirk.sh'),
        'SITEINFO_DOMAIN'   : getattr(settings, 'SITEINFO_DOMAIN', 'dirk.sh'),
        'SITEINFO_URL'      : getattr(settings, 'SITEINFO_URL', 'http://dirk.sh'),
        'SITEINFO_SUBTITLE' : getattr(settings, 'SITEINFO_SUBTITLE', ''),
        'DEFAULT_CHARSET'   : getattr(settings, 'DEFAULT_CHARSET', 'utf-8'),
    }
