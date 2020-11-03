from django.shortcuts import render
from .forms import UserForm
from .forms import StudentForm

import pymysql


# Create your views here.

def conn_db():
    # 获取数据库连接
    global conn
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cursor = conn.cursor()  # 获取一个游标
    return cursor


def studentManagement(request):
    username = request.session['username']
    cursor = conn_db()
    sql = "select * from student"
    cursor.execute(sql)
    # conn.commit()
    row_list = cursor.fetchall()
    cursor.close()
    return render(request, 'studentManagement.html', {"username": username, "row_list": row_list})


def studentAdd(request):
    username = request.session['username']
    if request.method == 'POST':
        studentform = StudentForm(request.POST)  # form包含提交的表单数据。
        if studentform.is_valid():
            sno = studentform.cleaned_data['sno']
            sname = studentform.cleaned_data['sname']
            spassword = studentform.cleaned_data['spassword']
            ssage = studentform.cleaned_data['ssage']
            ssex = studentform.cleaned_data['ssex']
            politics = studentform.cleaned_data['politics']
            phone = studentform.cleaned_data['phone']
            homeph = studentform.cleaned_data['homeph']
            address = studentform.cleaned_data['address']
            cet = studentform.cleaned_data['cet']
            compgrade = studentform.cleaned_data['compgrade']
            teachgrade = studentform.cleaned_data['teachgrade']
            mandarin = studentform.cleaned_data['mandarin']

            cursor = conn_db()
            sql1 = "insert into student values('%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                   % (sno, sname, spassword, ssage, ssex, politics, phone, homeph, address, cet, compgrade, teachgrade,
                      mandarin)
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from student"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'studentManagement.html', {"username": username, 'row_list': row_list})


def studentUpdated(request):
    username = request.session['username']
    if request.method == 'POST':
        studentform = StudentForm(request.POST)  # form包含提交的表单数据。
        if studentform.is_valid():
            sno = studentform.cleaned_data['sno']  # 通过input中name='sno'获取值。
            sname = studentform.cleaned_data['sname']
            spassword = studentform.cleaned_data['spassword']
            ssage = studentform.cleaned_data['ssage']
            ssex = studentform.cleaned_data['ssex']
            politics = studentform.cleaned_data['politics']
            phone = studentform.cleaned_data['phone']
            homeph = studentform.cleaned_data['homeph']
            address = studentform.cleaned_data['address']
            cet = studentform.cleaned_data['cet']
            compgrade = studentform.cleaned_data['compgrade']
            teachgrade = studentform.cleaned_data['teachgrade']
            mandarin = studentform.cleaned_data['mandarin']

            sql1 = "update student set sname = '%s', password = '%s', ssage = '%d', ssex = '%s', \
                                   politics = '%s', phone = '%s', homeph = '%s', address = '%s', \
                                   cet = '%s', compgrade = '%s', teachgrade = '%s', mandarin = '%s' \
                                   where sno = '%s' " % (sname, spassword, ssage, ssex, politics, phone, \
                                                         homeph, address, cet, compgrade, teachgrade, mandarin, sno)
            cursor = conn_db()
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from student"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'studentManagement.html', {"username": username, 'row_list': row_list})
        else:
            return render(request, 'studentManagement.html', {"username": username})
    else:
        return render(request, 'studentManagement.html', {"username": username})
