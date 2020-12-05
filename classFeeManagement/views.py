from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# from .forms import UserForm
from .forms import ClassFeeForm

import pymysql


# Create your views here.

def conn_db():
    # 获取数据库连接
    global conn
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cursor = conn.cursor()  # 获取一个游标
    return cursor


def classFeeManagement(request):
    username = request.session['username']
    cursor = conn_db()
    sql = "select * from fee"
    cursor.execute(sql)
    # conn.commit()
    row_list = cursor.fetchall()
    cursor.close()
    return render(request, 'classFeeManagement.html', {"username": username, "row_list": row_list})



def classFeeAdd(request):
    username = request.session['username']
    if request.method == 'POST':
        classFeeform = ClassFeeForm(request.POST)  # form包含提交的表单数据。
        if classFeeform.is_valid():
            fid = classFeeform.cleaned_data['fid']
            famount = classFeeform.cleaned_data['famount']
            fdate = classFeeform.cleaned_data['fdate']

            cursor = conn_db()
            sql1 = "insert into fee values('%s','%s','%s')" \
                   % (fid, famount, fdate)
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from fee"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'classFeeManagement.html', {"username": username, 'row_list': row_list})


def classFeeUpdated(request):
    username = request.session['username']
    if request.method=='POST':
        classFeeform = ClassFeeForm(request.POST) #form包含提交的表单数据。
        if classFeeform.is_valid():
            fid = classFeeform.cleaned_data['fid']
            famount = classFeeform.cleaned_data['famount']
            fdate = classFeeform.cleaned_data['fdate']

            sql1 = "update fee set famount = '%s', fdate = '%s'\
                                   where fid = '%s' " %(famount, fdate, fid)
            cursor = conn_db()
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from fee"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'classFeeManagement.html',{"username":username, 'row_list':row_list})
        else:
            return render(request, 'classFeeManagement.html',{"username":username})
    else:
        return render(request, 'classFeeManagement.html',{"username":username})



def classFeeDelete(request,fid):
    username = request.session['username']
    cursor = conn_db()
    sql1 = "delete from fee where fid='%s'" % fid
    cursor.execute(sql1)
    conn.commit()

    sql2 = "select * from fee"
    cursor.execute(sql2)
    row_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'classFeeManagement.html',{"username":username, 'row_list':row_list})


def classFeeSearch(request):
    if request.method == 'POST':
        username = request.session['username']
        fid = request.POST['fid']
        cursor = conn_db()
        if fid != '':
            sql1 = "select * from fee where fid = '%s'" %(fid)
            cursor.execute(sql1)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request,'classFeeManagement.html',{"username":username,'row_list':row_list})
        else:
            sql2 = "select * from fee"
            cursor.execute(sql2)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request,'classFeeManagement.html',{"username":username,'row_list':row_list})
        cursor.close()
        conn.close()