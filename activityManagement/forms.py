# -*- coding: utf-8 -*-
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class ActivityForm(forms.Form):
    aid = forms.CharField(required=True)  # aid必须和html中的aid对应
    atype = forms.ChoiceField(
        choices=(('班会', '班会'), ('团建', '团建'), ('其它', '其它')),
        label="活动类型",
        widget=forms.widgets.RadioSelect())
    atime = forms.CharField(widget=forms.TimeInput)
    members = forms.CharField(widget=forms.TextInput)