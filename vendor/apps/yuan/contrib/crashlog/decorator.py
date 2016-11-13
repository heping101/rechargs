# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  crashlog decorator

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

# pylint: disable = broad-except

import sys
import traceback
import socket
import warnings
import hashlib
from functools import wraps

from django.utils.decorators import available_attrs
from django.views.debug import ExceptionReporter

from .models import ErrorBatch, Error


def log_view_crash(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view_func(request, *args, **kwargs):
        try:
            return view_func(request, *args, **kwargs)
        except Exception, exception:
            log_context_crash(request, exception, u'decorator')

    return _wrapped_view_func


def log_context_crash(request, exception, catch_from=u'context'):
    server_name = socket.gethostname()
    tb_text = traceback.format_exc()
    class_name = exception.__class__.__name__
    checksum = hashlib.md5(tb_text).hexdigest()
    user_agent = request.META.get('HTTP_USER_AGENT')
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.META.get('REMOTE_ADDR')

    exc_type, exc_value, exc_traceback = sys.exc_info()
    exc_report = ExceptionReporter(request, exc_type, exc_value, exc_traceback)

    defaults = dict(
        class_name=class_name,
        message=exc_report.get_traceback_text(),
        url=request.build_absolute_uri(),
        server_name=server_name,
        traceback=tb_text,
        catch_from=catch_from,
        user_agent=user_agent,
        client_ip=client_ip,
    )

    try:
        Error.objects.create(** defaults)
        defaults.pop('catch_from')
        defaults.pop('user_agent')
        defaults.pop('client_ip')
        batch, created = ErrorBatch.objects.get_or_create(
            class_name=class_name,
            server_name=server_name,
            checksum=checksum,
            defaults=defaults
        )
        if not created:
            batch.times_seen += 1
            batch.save()
    except Exception, exc:
        warnings.warn(unicode(exc))
