# -*- coding: utf-8 -*-
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentForm(forms.Form):
    sno = forms.CharField(required=True)  # sno必须和html中的sno对应
    sname = forms.CharField(required=True)
    spassword = forms.CharField(widget=forms.PasswordInput)
    ssage = forms.IntegerField(required=True)
    ssex = forms.ChoiceField(
        choices=(('男', '男'), ('女', '女')),
        label="性别",
        widget=forms.widgets.RadioSelect()
    )

    politics = forms.ChoiceField(
        choices=(('团员', '团员'), ('党员', '党员')),
        label="政治面貌",
        widget=forms.widgets.RadioSelect()
    )
    phone = forms.CharField(required=True)
    homeph = forms.CharField(required=True)
    address = forms.CharField(required=True)
    cet = forms.ChoiceField(
        choices=(('四级', '四级'), ('六级', '六级'), ('无', '无')),
        label="cet",
        widget=forms.widgets.RadioSelect())
    compgrade = forms.ChoiceField(
        choices=(('1级', '2级'), ('2级', '2级'), ('3级', '3级'), ('4级', '4级'), ('无', '无')),
        label="计算机等级",
        widget=forms.widgets.RadioSelect())
    teachgrade = forms.ChoiceField(
        choices=(('助教', '助教'), ('讲师', '讲师'), ('副教授', '副教授'), ('教授', '教授')),
        label="教师等级",
        widget=forms.widgets.RadioSelect())
    mandarin = forms.ChoiceField(
        choices=(
        ('一级甲等', '一级甲等'), ('一级乙等', '一级乙等'), ('二级甲等', '二级甲等'), ('二级乙等', '二级乙等'), ('三级甲等', '三级甲等'), ('三级乙等', '三级乙等'),
        ('无', '无')),
        label="普通话等级",
        widget=forms.widgets.RadioSelect())
