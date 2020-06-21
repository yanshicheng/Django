#!/usr/bin/python
# -*- coding: UTF-8 -*-

from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from app01.models import GENDER_CHOICES,UserInfo

class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        min_length=4,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': '用户名',
            }
        ),
        error_messages={
            "required": "用户名不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最小为4位",
            "max_length": "用户名最长为16位",
        }
    )

    password = forms.CharField(
        max_length=24,
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={
                'placeholder':'密  码',
            }
        ),

        error_messages={
            "required": "密码不能为空",
            "invalid": "格式错误",
            "min_length": "密码最小为6位",
            "max_length": "密码最长为24位",
        }
    )
    re_password = forms.CharField(
        max_length=24,
        min_length=6,
        widget=forms.widgets.PasswordInput(
            attrs={
                'placeholder': '确认密码',
            }
        ),

        error_messages={
            "required": "密码不能为空",
            "invalid": "格式错误",
            "min_length": "密码最小为6位",
            "max_length": "密码最长为24位",
        }
    )
    phone = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.widgets.TextInput(
            attrs={
                'placeholder': '手机号',
            }
        ),
        validators=[RegexValidator(r'^1[3-9]\d{9}$',)],
        error_messages={
            "required": "手机号不能为空",
            "invalid": "请输入正确手机号",
            "min_length": "请输入正确手机号",
            "max_length": "请输入正确手机号",
        }
    )
    email = forms.CharField(
        widget=forms.widgets.EmailInput(
            attrs={
                'placeholder': '邮  箱',
            }
        ),
        validators=[RegexValidator(r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"),],
        error_messages={
            "required": "邮箱不能为空",
            "invalid": "请输入正确邮箱地址",
            "min_length": "请输入正确邮箱地址",
            "max_length": "请输入正确邮箱地址",
        }
    )
    gender = forms.ChoiceField(
        label='性别',
        widget=forms.widgets.RadioSelect(),
        choices=GENDER_CHOICES,
        initial=0,
        error_messages={
            "required": "性别不能为空",
            "invalid": "格式错误",
        }
    )

    # 写一个局部钩子方法,校验用户名是否已经被注册
    def clean_username(self):
        name_value = self.cleaned_data.get('username')
        is_exist = UserInfo.objects.filter(username=name_value)
        if is_exist:
            raise ValidationError('用户名已经存在')
        else:
            return name_value
    # 写一个局部钩子方法,校验手机号是否已经被注册
    def clean_phone(self):
        phone_value = self.cleaned_data.get('phone')
        is_exist = UserInfo.objects.filter(phone=phone_value)
        if is_exist:
            raise ValidationError('手机号已经存在')
        else:
            return phone_value
    # 写一个局部钩子方法,校验邮箱是否已经被注册
    def clean_email(self):
        email_value = self.cleaned_data.get('email')
        is_exist = UserInfo.objects.filter(email=email_value)
        if is_exist:
            raise ValidationError('邮箱已经存在')
        else:
            return email_value

    # 判断密码是否输入一致
    def clean(self):
        # 所有经过校验的数据 self.cleaned_data
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data # 一致则返回数据
        else:
            self.add_error('re_password','两次密码不一致')
            raise ValidationError('两次密码不一致')
    # 初始化添加循环添加类
    def __init__(self,*args,**kwargs):
        super(RegForm,self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            # 如果是 gender 则跳过
            if field == 'gender':
                continue
            self.fields[field].widget.attrs.update({
                'class':'input-material',
            })