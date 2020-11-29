from django.shortcuts import render
from .forms import UserForm
from .forms import LeaveForm
# from django.views.decorators.csrf import csrf_exempt

import pymysql


# Create your views here.

def conn_db():
    # 获取数据库连接
    global conn
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cursor = conn.cursor()  # 获取一个游标
    return cursor


def leaveManagement(request):
    username = request.session['username']
    cursor = conn_db()
    sql = "select * from student.leave"
    cursor.execute(sql)
    # conn.commit()
    row_list = cursor.fetchall()
    cursor.close()
    return render(request, 'leaveManagement.html', {"username": username, "row_list": row_list})

def leaveAdd(request):
    username = request.session['username']
    if request.method == 'POST':
        leaveform = LeaveForm(request.POST)  # form包含提交的表单数据。
        if leaveform.is_valid():
            lid = leaveform.cleaned_data['lid']
            ltype = leaveform.cleaned_data['ltype']
            ltime = leaveform.cleaned_data['ltime']
            ldate = leaveform.cleaned_data['ldate']
            lplace = leaveform.cleaned_data['lplace']

            cursor = conn_db()
            sql1 = "insert into student.leave values('%s','%s','%s','%s','%s')" \
                   % (lid, ltype, ltime, ldate, lplace)
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from student.leave"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'leaveManagement.html', {"username": username, 'row_list': row_list})


def leaveUpdated(request):
    username = request.session['username']
    if request.method=='POST':
        leaveform = LeaveForm(request.POST) #form包含提交的表单数据。
        if leaveform.is_valid():
            lid = leaveform.cleaned_data['lid']
            ltype = leaveform.cleaned_data['ltype']
            ltime = leaveform.cleaned_data['ltime']
            ldate = leaveform.cleaned_data['ldate']
            lplace = leaveform.cleaned_data['lplace']

            sql1 = "update student.leave set ltype = '%s', ltime = '%s', ldate = '%s', lplace = '%s'\
                                   where lid = '%s' " %(ltype, ltime, ldate, lplace, lid)
            cursor = conn_db()
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from student.leave"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'leaveManagement.html',{"username":username, 'row_list':row_list})
        else:
            return render(request, 'leaveManagement.html',{"username":username})
    else:
        return render(request, 'leaveManagement.html',{"username":username})

def leaveDelete(request,lid):
    username = request.session['username']
    cursor = conn_db()
    sql1 = "delete from student.leave where lid='%s'" %(lid)
    cursor.execute(sql1)
    conn.commit()

    sql2 = "select * from student.leave"
    cursor.execute(sql2)
    row_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'leaveManagement.html',{"username":username, 'row_list':row_list})


def leaveSearch(request):
    if request.method == 'POST':
        username = request.session['username']
        ltype = request.POST['ltype']
        cursor = conn_db()
        if ltype != '':
            sql1 = "select * from student.leave where ltype = '%s'" % (ltype)
            cursor.execute(sql1)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request, 'leaveManagement.html', {"username": username, 'row_list': row_list})
        else:
            sql2 = "select * from student.leave"
            cursor.execute(sql2)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request, 'leaveManagement.html', {"username": username, 'row_list': row_list})
            cursor.close()