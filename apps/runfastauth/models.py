# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""

from django.db import models

from seller.models import Sellers


USER_GENDER_AS_UNKNOWN = 0
USER_GENDER_AS_MALE = 1
USER_GENDER_AS_FEMALE = 2

USER_GENDER_CHOICES = (
    (USER_GENDER_AS_UNKNOWN, u'未知'),
    (USER_GENDER_AS_MALE, u'男'),
    (USER_GENDER_AS_FEMALE, u'女')
)


class Users(models.Model):
    """ 用户 """
    wx_openid = models.CharField(u'OpenId', max_length=200, db_index=True)
    wx_name = models.CharField(u'昵称', max_length=100, db_index=True)
    wx_avatar = models.CharField(u'头像', max_length=300)
    wx_gender = models.PositiveSmallIntegerField(u'性别', choices=USER_GENDER_CHOICES, default=USER_GENDER_AS_UNKNOWN, db_index=True)
    agent_id = models.ForeignKey(Sellers, verbose_name=u'所属代理', blank=True, null=True)
    topic_id = models.CharField(u'主题ID', max_length=64)
    apm = models.PositiveIntegerField(u"手速", default=0)
    room_cards = models.PositiveIntegerField(u'房卡数量', default=0)
    is_forbidden = models.BooleanField(u'用户被禁用', default=False)
    is_vip = models.BooleanField(u'VIP用户', default=False)
    full_name = models.CharField(u'真实姓名', max_length=100, blank=True, db_index=True)
    phone_num = models.CharField(u'联系电话', max_length=20, blank=True)
    address = models.CharField(u'联系地址', blank=True, max_length=300)
    total_rounds = models.PositiveIntegerField(u'总场次', default=0)
    win_rounds = models.PositiveIntegerField(u'胜利场次', default=0)
    score = models.PositiveIntegerField(u'得分', default=0)
    client_ip = models.CharField(u'IP', max_length=20, db_index=True)
    imei = models.CharField(u'手机串号', max_length=45)
    last_login = models.PositiveIntegerField(u'登录时间', default=0, db_index=True)
    joined_since = models.PositiveIntegerField(u'加入时间', default=0, db_index=True)

    def __unicode__(self):
        return u"%s<%s>" % (self.wx_name, self.pk)

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户'
        db_table = 'users'
