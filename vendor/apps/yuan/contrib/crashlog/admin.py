# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  admin interface

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.contrib import admin

from .models import ErrorBatch, Error


class ErrorBatchAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'url', 'times_seen', 'last_seen', 'server_name')
    list_filter = ('class_name', 'times_seen', 'server_name')
    ordering = ('-last_seen',)

    def has_add_permission(self, request):
        return False


class ErrorAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'url', 'catch_from', 'client_ip', 'user_agent', 'datetime', 'server_name')
    list_filter = ('catch_from', 'class_name', 'server_name')
    date_hierarchy = 'datetime'
    ordering = ('-datetime',)

    def has_add_permission(self, request):
        return False

admin.site.register(ErrorBatch, ErrorBatchAdmin)
admin.site.register(Error, ErrorAdmin)
