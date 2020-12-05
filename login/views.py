# -*- coding: utf-8 -*-
from .forms import UserForm  # .表示当前目录
from django.shortcuts import render

import pymysql


# Create your views here.

def conn():
    # 获取数据库连接
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cursor = conn.cursor()  # 获取一个游标
    return cursor


def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)  # form包含提交的表单数据。
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            # role = userform.cleaned_data['role']
            request.session['username'] = username

            cursor = conn()

            sql = "select * from teacher where sname = '%s' and password = '%s'" % (username, password)

            try:
                cursor.execute(sql)
                user = cursor.fetchone()
                cursor.close()  # 释放游标
                if user:
                    return render(request, "studentManagement.html", {"username": username})
                else:
                    return render(request, 'loginError.html')
            except Exception as e:
                print(e)
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')
