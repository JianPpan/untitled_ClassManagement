from django.shortcuts import render
from .forms import UserForm
from .forms import ActivityForm
# from django.views.decorators.csrf import csrf_exempt

import pymysql


# Create your views here.

def conn_db():
    # 获取数据库连接
    global conn
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='student', port=3306, charset='utf8')
    cursor = conn.cursor()  # 获取一个游标
    return cursor


def activityManagement(request):
    username = request.session['username']
    cursor = conn_db()
    sql = "select * from activity"
    cursor.execute(sql)
    # conn.commit()
    row_list = cursor.fetchall()
    cursor.close()
    return render(request, 'activityManagement.html', {"username": username, "row_list": row_list})

def activityAdd(request):
    username = request.session['username']
    if request.method == 'POST':
        activityform = ActivityForm(request.POST)  # form包含提交的表单数据。
        if activityform.is_valid():
            aid = activityform.cleaned_data['aid']
            atype = activityform.cleaned_data['atype']
            atime = activityform.cleaned_data['atime']
            members = activityform.cleaned_data['members']

            cursor = conn_db()
            sql1 = "insert into activity values('%s','%s','%s','%s')" \
                   % (aid, atype, atime, members )
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from activity"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'activityManagement.html', {"username": username, 'row_list': row_list})

def activityUpdated(request):
    username = request.session['username']
    if request.method=='POST':
        activityform = ActivityForm(request.POST) #form包含提交的表单数据。
        if activityform.is_valid():
            aid = activityform.cleaned_data['aid']
            atype = activityform.cleaned_data['atype']
            atime = activityform.cleaned_data['atime']
            members = activityform.cleaned_data['members']

            sql1 = "update activity set atype = '%s', atime = '%s', members = '%s'\
                                   where aid = '%s' " %(atype, atime, members, aid)
            cursor = conn_db()
            cursor.execute(sql1)
            conn.commit()

            sql2 = "select * from activity"
            cursor.execute(sql2)
            row_list = cursor.fetchall()
            cursor.close()
            conn.close()
            return render(request, 'activityManagement.html',{"username":username, 'row_list':row_list})
        else:
            return render(request, 'activityManagement.html',{"username":username})
    else:
        return render(request, 'activityManagement.html',{"username":username})

def activityDelete(request,aid):
    username = request.session['username']
    cursor = conn_db()
    sql1 = "delete from activity where aid='%s'" %(aid)
    cursor.execute(sql1)
    conn.commit()

    sql2 = "select * from activity"
    cursor.execute(sql2)
    row_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return render(request, 'activityManagement.html',{"username":username, 'row_list':row_list})


def activitySearch(request):
    if request.method=='POST':
        username = request.session['username']
        atype = request.POST['atype']
        cursor = conn_db()
        if atype!='':
            sql1="select * from activity where atype = '%s'"%(atype)
            cursor.execute(sql1)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request,'activityManagement.html',{"username":username,'row_list':row_list})
        else:
            sql2 = "select * from activity"
            cursor.execute(sql2)
            conn.commit()
            row_list = cursor.fetchall()
            return render(request,'activityManagement.html',{"username":username,'row_list':row_list})
        cursor.close()
        conn.close()