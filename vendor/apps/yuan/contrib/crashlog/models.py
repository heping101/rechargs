# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  相关的数据库模型定义

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ErrorBatch(models.Model):
    class_name = models.CharField(_('Type'), max_length=128)
    traceback = models.TextField()
    message = models.TextField()
    times_seen = models.PositiveIntegerField(default=1)
    last_seen = models.DateTimeField(auto_now=True)
    first_seen = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    server_name = models.CharField(max_length=128, db_index=True)
    checksum = models.CharField(max_length=32, db_index=True)

    def __unicode__(self):
        return self.class_name

    class Meta:
        unique_together = (('class_name', 'server_name', 'checksum'),)


class Error(models.Model):
    class_name = models.CharField(_('type'), max_length=128, db_index=True)
    traceback = models.TextField()
    message = models.TextField()
    catch_from = models.CharField(_('Catch from'), max_length=10, db_index=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, db_index=True)
    url = models.URLField(null=True, blank=True)
    user_agent = models.CharField(max_length=300, null=True, blank=True)
    client_ip = models.CharField(max_length=50, null=True, blank=True)
    server_name = models.CharField(max_length=128, db_index=True)

    def __unicode__(self):
        return self.class_name
