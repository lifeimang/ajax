from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from datetime import datetime, timedelta
# Create your views here.


# /index
def index(request):
    """首页"""
    # 使用模板
    # return HttpResponse('首页')
    # render方法的返回值就是HttpResponse类的对象
    # return render(request, 'booktest/index.html')

    i = 0
    i += 1
    return HttpResponse(i)


# /showarg数字
def show_arg(request, num1):
    """位置参数捕获"""
    return HttpResponse(num1)


# /showkwarg数字
def show_kwarg(request, num):
    """关键字参数捕获"""
    return HttpResponse(num)

# request参数是HttpRequest类的实例对象
# request参数包含浏览器请求的信息
# request.POST->保存post提交的参数
# request.GET->保存get提交的参数


# 表单提交数据的方式: get提交 post提交
# 提交表单时，向action指定的地址发起提交请求
# get提交：参数在地址栏
# post提交：参数在请求报文中
# 如果涉及到安全数据，不要使用get提交
# 如果提交的参数过多的时候，不要使用get提交

# 表单提交时，如果表单中的checkbox没有被选中，则值不会被提交
# /login
def login(request):
    """显示登录页面"""
    # 获取cookie username
    if 'username' in request.COOKIES:
        # 记住了用户名
        username = request.COOKIES['username']
        checked = 'checked'
    else:
        username = ''
        checked = ''

    # 使用模板
    return render(request, 'booktest/login.html', {'username': username, 'checked': checked})


# /login_check
def login_check_1(request):
    """登录验证"""
    # <class 'django.http.request.QueryDict'>
    # QueryDict类似字典，但是允许一个名字对应多个值
    # 获取一个名字对应的多个值时，需要使用getlist方式
    # print(type(request.POST))
    # print(type(request.GET))
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # print(username+':'+password)

    # 实际开发：根据username和password去查询数据库
    # 模拟登录：username == 'smart' and password == '123'
    if username == 'smart' and password == '123':
        # 用户名密码正确：跳转首页
        # return HttpResponse('用户密码正确')
        # return HttpResponseRedirect('/index')
        return redirect('/index')
    else:
        # 用户名或密码错误，跳转的登录页面
        # return HttpResponse('用户或密码错误')
        # return HttpResponseRedirect('/login')
        return redirect('/login')


# /ajax_test
def ajax_test(request):
    """ajax页面"""
    return render(request, 'booktest/ajax_test.html')


# /ajax_handle
def ajax_handle(request):
    """ajax请求处理"""
    # 获取参数
    name = request.GET.get('name')

    # 返回json数据
    return JsonResponse({'name': name})


# /login_ajax
def login_ajax(request):
    """显示ajax登录页面"""
    return render(request, 'booktest/login_ajax.html ')  # 注意字符串内是否拼写错误是否含有空格


# 前端ajax post请求
# 传递参数: username password
# /login_ajax_check
def login_ajax_check(request):
    """ajax登录验证"""
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 登录验证
    # 模拟登录：username == 'smart' and password == '123'
    if username == 'smart' and password == '123':
        # 用户名密码正确 {'res': 1}
        return  JsonResponse({'res': 1})
    else:
        # 用户名或密码错误 {'res': 0}
        return JsonResponse({'res': 0})


# /set_cookie
def set_cookie(request):
    """设置cookie信息"""
    # 创建HttpResponse类对象
    response = HttpResponse('设置cookie信息')

    # 设置cookie信息，key->'username' value->'smart'
    # max_age代表cookie多少秒之后过期
    # response.set_cookie('username', 'smart', max_age=7*24*3600)
    response.set_cookie('username', 'smart', expires=datetime.utcnow()+timedelta(days=7))
    # 设置cookie信息，key->'age' value->18
    # response.set_cookie('age', 18, max_age=7*24*3600)
    response.set_cookie('age', 18, expires=datetime.utcnow() + timedelta(days=7))
    # 返回response
    return response


# /get_cookie
def get_cookie(request):
    """获取cookie信息"""
    # 浏览器发送给网站服务器的cookie信息，都保存在request.COOKIES字典中
    # 获取cookie username
    username = request.COOKIES['username']
    # 获取cookie age
    age = request.COOKIES['age']

    # 返回应答
    return HttpResponse(username+':'+age)


def login_check(request):
    """登录验证"""
    # 获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 实际开发：根据username和password去查询数据库
    # 模拟登录：username == 'smart' and password == '123'
    if username == 'smart' and password == '123':
        # 用户名密码正确：跳转首页
        response = redirect('/index')  # HttpResponseRedirect
        # 判断是否需要记住用户名
        remember = request.POST.get('remember')

        if remember == 'on':
            # 记住用户名，设置一个cookie username, 值为用户输入的username
            # HttpResponse是HttpResponseRedirect和JsonResponse类的父类
            response.set_cookie('username', username, max_age=7*24*3600)
        else:
            # 不需要记住用户名,删除cookie username
            response.delete_cookie('username')

        return response
    else:
        # 用户名或密码错误，跳转的登录页面
        return redirect('/login')








