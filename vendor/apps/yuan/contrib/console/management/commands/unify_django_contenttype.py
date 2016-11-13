# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  Management commands added to django-admin.py

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

# pylint: disable = protected-access

from django.core.management.base import BaseCommand

from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Unify Django contenttype name according to app models' verbose_name."

    def handle(self, *args, **options):
        for ctype in ContentType.objects.all():
            if not ctype.model_class():
                print "Delete outmoded Contentype [%s]" % (unicode(ctype.name).encode('utf-8'), )
                ctype.delete()
                continue
            vname = ctype.model_class()._meta.verbose_name
            if ctype.name != vname:
                print "Unify [%s] to [%s]" % (unicode(ctype.name).encode('utf-8'), unicode(vname).encode('utf-8'))
                ctype.name = vname
                ctype.save()
