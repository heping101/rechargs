# -*- coding: utf-8 -*-

"""
  recharge version 1.0

  @author wangyonghui <wangyonghuimail@163.com>
  @copyright Copyright (c) 2016 runfast.cn
  @link http://runfast.cn
"""
from django.contrib.auth.hashers import check_password, make_password
from django.db import models
from django.utils.crypto import salted_hmac

SELLER_TYPE_AS_DAILI = 1
SELLER_TYPE_AS_ADMIN = 2

SELLER_TYPE_CHOICES = (
    (SELLER_TYPE_AS_DAILI, u'代理'),
    (SELLER_TYPE_AS_ADMIN, u'管理员'),
)


class Sellers(models.Model):
    """代理"""

    USERNAME_FIELD = 'name'
    name = models.CharField(u'姓名', max_length=200, db_index=True)
    password = models.CharField(u'密码', max_length=100)
    address = models.CharField(u'联系地址', max_length=300)
    phone_num = models.CharField(u'联系电话', max_length=20, blank=True)
    room_cards = models.PositiveIntegerField(u'房卡数量', default=0)
    status = models.CharField(u'在职状态', max_length=100, db_index=True)
    seller_type = models.PositiveSmallIntegerField(u'卖家类型', choices=SELLER_TYPE_CHOICES, default=SELLER_TYPE_AS_DAILI,
                                                   db_index=True)
    utime = models.PositiveIntegerField(u'更新时间', default=0, db_index=True)
    ctime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True)

    def __unicode__(self):
        return u"%s<%s>" % (self.name, self.pk)

    class Meta:
        verbose_name = u'代理与管理员'
        verbose_name_plural = u'代理与管理员'
        db_table = 'sellers'

    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.get_username()

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])

        return check_password(raw_password, self.password, setter)

    def get_session_auth_hash(self):
        """
        Returns an HMAC of the password field.
        """
        key_salt = "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash"
        return salted_hmac(key_salt, self.passwd).hexdigest()


BUYER_TYPE_AS_USER = 1
BUYER_TYPE_AS_VIP = 2
BUYER_TYPE_AS_DAILI = 3

BUYER_TYPE_CHOICES = (
    (BUYER_TYPE_AS_USER, u'普通用户'),
    (BUYER_TYPE_AS_VIP, u'会员'),
    (BUYER_TYPE_AS_DAILI, u'代理'),
)


class SaleRecord(models.Model):
    """售卖记录"""
    seller_id = models.ForeignKey(Sellers, verbose_name=u'卖家', db_index=True)
    buyer_id = models.PositiveIntegerField(u'买家ID')
    buyer_type = models.PositiveSmallIntegerField(u'买家类型', choices=BUYER_TYPE_CHOICES, default=BUYER_TYPE_AS_USER,
                                                  db_index=True)
    cards_num = models.PositiveIntegerField(u'房卡数量', default=0)
    room_cards = models.PositiveIntegerField(u'房卡数量', default=0)
    total_money = models.CharField(u'总金额', max_length=100, db_index=True, help_text=u'总金额， 以分为单位')
    utime = models.PositiveIntegerField(u'更新时间', default=0, db_index=True)
    ctime = models.PositiveIntegerField(u'创建时间', default=0, db_index=True)

    def __unicode__(self):
        return u"%s<%s>" % (self.name, self.pk)

    class Meta:
        verbose_name = u'售卖记录'
        verbose_name_plural = u'售卖记录'
        db_table = 'sale_record'
