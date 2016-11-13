# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  后端验证相关的函数.

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class ConsoleModelBackend(ModelBackend):
    """
    使用EMail和密码验证用户 django.contrib.auth.models.User
    """
    # TODO: Model, login attribute name and password attribute name should be configurable.
    def authenticate(self, email=None, password=None, **kwargs):
        if "typo_check" in kwargs.keys():
            # Mistakenly entered username instead of e-mail address? Look it up.
            try:
                user = User.objects.get(username=email)
                if user.check_password(password):
                    return user
            except (User.DoesNotExist, User.MultipleObjectsReturned):
                # Nothing to do here, moving along.
                pass
        else:
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                pass
        return None
