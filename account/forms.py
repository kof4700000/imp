# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    '''
    Form 检查流程：clean每个Field，如果失败则raise ValidationError,然后收集
    到Form中，如果没有error返回self.clean_data，否则返回ErrorDict类型的self.error
    查看django/forms/forms.py，jango/forms/fields.py代码，很详细
    is_valid -> self.errors -> self.full_clean -> self._clean_fields ...
    '''
    username = forms.CharField(label='username',
                               max_length=20,
                               #in Field.py:
                               #    Field.clean -> Field.validate:
                               #        raise ValidationError(self.error_messages['required'])
                               #传入Field的是空值，返回错误信息的键为'required'
                               error_messages={'required':'Please enter your name'})
    password = forms.CharField(label='password', max_length=20)
