# -*- coding: utf-8 -*-
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class LeaveForm(forms.Form):
    lid = forms.CharField(required=True)  # aid必须和html中的aid对应
    ltype = forms.ChoiceField(
        choices=(('事假', '事假'), ('病假', '病假'), ('其它', '其它')),
        label="请假类型",
        widget=forms.widgets.RadioSelect())
    ltime = forms.CharField(widget=forms.TimeInput)
    ldate = forms.CharField(widget=forms.TextInput)
    lplace = forms.CharField(widget=forms.TextInput)