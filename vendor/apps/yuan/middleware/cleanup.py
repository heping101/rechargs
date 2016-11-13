# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  cleanup middlewares

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import re


class StripWhitespaceMiddleware(object):
    """
    Tightens up response content by removed superflous line breaks and leading whitespace.
    """
    def __init__(self):
        self.cleanup = re.compile(r'>[\r\n]+\s*<')

    def process_response(self, request, response):
        # if 'text/html' in response.headers.get('Content-Type', '').lower():
        #     print dir(response)
        #     print response.headers
        if (response.has_header('Content-Type')) and ("text" in response['Content-Type']):
            from django.conf import settings
            if settings.DEBUG:
                new_content = self.cleanup.sub('>\n<', response.content)
            else:
                new_content = self.cleanup.sub('><', response.content)
            response.content = new_content
        return response


class WMLStripWhitespaceMiddleware(object):
    """
    for text/vnd.wap.wml
    Tightens up response content by removed superflous line breaks and leading whitespace.
    """
    def __init__(self):
        self.cleanup = re.compile(r'>[\r\n]+\s*')

    def process_response(self, request, response):
        # if 'text/html' in response.headers.get('Content-Type', '').lower():
        #     print dir(response)
        #     print response.headers
        # if ("text" in response['Content-Type']):
        if (response.has_header('Content-Type')) and (response['Content-Type'].lower() == 'text/vnd.wap.wml'):
            from django.conf import settings
            if settings.DEBUG:
                new_content = self.cleanup.sub('>\n', response.content)
            else:
                new_content = self.cleanup.sub('>', response.content)
            response.content = new_content
        return response
