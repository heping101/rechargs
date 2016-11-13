# -*- coding: utf-8 -*-

"""
  yuan.dirk.sh version 1.0

  根据接口特性进行一定封装的Form基类

  @author Dirk Ye <dirk.ye@gmail.com>
  @copyright Copyright (c) 2008 - 2015 dirk.sh
  @link http://www.dirk.sh
"""

from django import forms
from django.core.exceptions import ValidationError


class YuanForm(forms.Form):
    _error_code = 98  # 默认为数据非法
    _error_msg = u''

    def raiseValidationError(self, errcode, errmsg):
        self._error_code = errcode
        self._error_msg = errmsg
        raise forms.ValidationError(errmsg)

    @property
    def error_code(self):
        return self._error_code

    @property
    def error_message(self):
        if self._error_code == 98:
            return self.errors.as_text()
        else:
            return self._error_msg


class YuanModelForm(forms.ModelForm):
    _error_code = 98
    _error_msg = u''

    def raiseValidationError(self, errcode, errmsg):
        self._error_code = errcode
        self._error_msg = errmsg
        raise ValidationError(errmsg)

    @property
    def error_code(self):
        return self._error_code

    @property
    def error_message(self):
        if self._error_code == 98:
            return self.errors.as_text()
        else:
            return self._error_msg


class MultiFileInput(forms.FileInput):
    def render(self, name, value, attrs=None):
        if not isinstance(attrs, dict):
            attrs = {}
        attrs['multiple'] = 'multiple'
        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        else:
            return [files.get(name)]


class MultiFileField(forms.FileField):
    widget = MultiFileInput
    default_error_messages = {
        'min_num': u"Ensure at least %(min_num)s files are uploaded (received %(num_files)s).",
        'max_num': u"Ensure at most %(max_num)s files are uploaded (received %(num_files)s).",
        'file_size': u"File: %(uploaded_file_name)s, exceeded maximum upload size."
    }

    def __init__(self, *args, **kwargs):
        self.min_num = kwargs.pop('min_num', 0)
        self.max_num = kwargs.pop('max_num', None)
        self.maximum_file_size = kwargs.pop('maximum_file_size', None)
        super(MultiFileField, self).__init__(*args, **kwargs)

    def to_python(self, data):
        ret = []
        for item in data:
            ret.append(super(MultiFileField, self).to_python(item))
        return ret

    def validate(self, data):
        super(MultiFileField, self).validate(data)
        num_files = len(data)
        if len(data) and not data[0]:
            num_files = 0
        if num_files < self.min_num:
            raise ValidationError(self.error_messages['min_num'] % {'min_num': self.min_num, 'num_files': num_files})
        elif self.max_num and num_files > self.max_num:
            raise ValidationError(self.error_messages['max_num'] % {'max_num': self.max_num, 'num_files': num_files})
        for uploaded_file in data:
            if uploaded_file.size > self.maximum_file_size:
                raise ValidationError(self.error_messages['file_size'] % {'uploaded_file_name': uploaded_file.name})
