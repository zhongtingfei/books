from django import forms
from django.core.exceptions import ValidationError


class userForm(forms.Form):
    #用户名
    uname = forms.CharField(
        min_length=3,
        label='用户名',
        error_messages={
            "required" : "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短3位"
        },
        widget=forms.TextInput(attrs={'class':'layui-input'})
    )
    #密码
    upasswd = forms.CharField(
        min_length=3,
        label="密码",
        error_messages={
            "required": "不能为空",
            "min_length": "密码最短3位"
        },
        widget=forms.PasswordInput(attrs={'class': 'layui-input'})
    )
    #确认密码
    re_upasswd = forms.CharField(
        min_length=3,
        label="确认密码",
        error_messages={
            "required": "不能为空",
            "min_length": "密码最短3位"
        },
        widget=forms.PasswordInput(attrs={'class': 'layui-input'})
    )

    uemail = forms.EmailField(
        label="邮箱地址",
        error_messages={
            "required": "不能为空",
        },
        widget=forms.EmailInput(attrs={'class': 'layui-input'})
    )

