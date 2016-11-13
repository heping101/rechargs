# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  试图修正 logging.handlers.RotatingFileHandler 的日志文件所有者权限不正常问题

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

import os
import platform

from logging.handlers import RotatingFileHandler


class RotatingFileWithOwnerHandler(RotatingFileHandler):
    owner_uid = 0
    owner_gid = 0

    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=0, **kwargs):
        try:
            self.owner_uid = kwargs.get('uid', 65534)
            self.owner_gid = kwargs.get('gid', 65534)
        except KeyError:
            pass
        RotatingFileHandler.__init__(self, filename, mode=mode, maxBytes=maxBytes, backupCount=backupCount, encoding=encoding, delay=delay)

    def _open(self):
        prevumask = os.umask(0o002)
        rtv = RotatingFileHandler._open(self)
        os.umask(prevumask)
        try:
            if platform.system() != "Windows":
                os.chown(self.baseFilename, self.owner_uid, self.owner_gid)
        except OSError:
            pass
        return rtv
