# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""

from django.db import models

from runfastauth.models import Users

ROOM_STATUS_AS_UNUSED = 0
ROOM_STATUS_AS_USING = 1
ROOM_STATUS_AS_DISBAND = 2


ROOM_STATUS_CHOICES = (
    (ROOM_STATUS_AS_UNUSED, u'未使用'),
    (ROOM_STATUS_AS_USING, u'使用中'),
    (ROOM_STATUS_AS_DISBAND, u'已解散'),
)


class Rooms(models.Model):
    """房间"""
    id = models.CharField(primary_key=True, max_length=5)
    creator = models.ForeignKey(Users, verbose_name=u'创建者', db_index=True)
    pointer = models.ForeignKey(Users, verbose_name=u'指针', blank=True, null=True, db_index=True)
    l_cards = models.CharField(u'上家出得牌', max_length=20, blank=True)
    g_num = models.PositiveIntegerField(u'局数', default=0)
    disband = models.BooleanField(u'是否同意解散', default=False, db_index=True)
    args = models.TextField(u'统计步骤')
    status = models.CharField(u'房间状态', choices=ROOM_STATUS_CHOICES, default=ROOM_STATUS_AS_UNUSED, db_index=True)
    utime = models.PositiveIntegerField(u'更新时间', default=0, db_index=True)
    ctime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True)

    def __unicode__(self):
        return u"%s<%s>" % (self.name, self.pk)

    class Meta:
        verbose_name = u'房间'
        verbose_name_plural = u'房间'
        db_table = 'rooms'


class UserRooms(models.Model):
    """房间玩家"""
    r_id = models.ForeignKey(Users, verbose_name=u'创建者', db_index=True)
    u_id = models.ForeignKey(Users, verbose_name=u'指针', blank=True, null=True, db_index=True)
    g_num = models.PositiveIntegerField(u'局数', default=0)
    bomb = models.PositiveSmallIntegerField(u'炸弹数', default=0)
    location = models.PositiveSmallIntegerField(u'玩家位置', help_text=u'1下方 2右方 3左方')
    process = models.CharField(u'出过的牌', max_length=150, blank=True)
    cards = models.CharField(u'剩余牌', max_length=100, blank=True)
    mark = models.IntegerField(u'得分', default=0, help_text=u'赢为正数， 输为负数')
    status = models.BooleanField(u'是否在线', default=True, db_index=True)
    utime = models.PositiveIntegerField(u'更新时间', default=0, db_index=True)
    ctime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True)

    def __unicode__(self):
        return u"%s<%s>" % (self.name, self.pk)

    class Meta:
        verbose_name = u'房间玩家'
        verbose_name_plural = u'房间玩家'
        db_table = 'user_rooms'
