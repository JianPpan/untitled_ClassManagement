# -*- coding: utf-8 -*-

from django import forms
# from classFeeManagement import forms

#
# class UserForm(forms.Form):
#     username = forms.CharField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput)


class ClassFeeForm(forms.Form):
    fid = forms.CharField(required=True)  # fid必须和html中的fid对应
    famount = forms.ChoiceField(
        choices=(('8000', '8000'), ('9999', '9999'), ('10000', '10000')),
        label="班费金额",
        widget=forms.widgets.RadioSelect())
    fdate = forms.ChoiceField(
        choices=(('2020.11.11', '2020.11.11'), ('2020.12.12', '2020.12.12'), ('2020.12.31', '2020.12.31')),
        label="统计时间",
        widget=forms.widgets.RadioSelect())
