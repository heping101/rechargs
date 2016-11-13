# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  crashlog middlewares

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from .decorator import log_context_crash


class CrashLogMiddleware(object):

    def process_exception(self, request, exception):
        log_context_crash(request, exception, u'middleware')
