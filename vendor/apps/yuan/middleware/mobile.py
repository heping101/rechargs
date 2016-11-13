# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  mobile middlewares

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""


class MobileClientMiddleware(object):
    def process_request(self, request):
        in_iosdevice = False
        in_mobile = False
        if 'HTTP_USER_AGENT' in request.META:
            agents = request.META['HTTP_USER_AGENT'].lower()
            in_iosdevice = ('iphone' in agents) or ('ipad' in agents) or ('android' in agents)
            in_mobile = ('iphone' in agents) or ('android' in agents)

        request.IS_IOS_DEVICE = in_iosdevice
        request.IS_MOBILE_CLIENT = in_mobile
