from django.conf.urls import url
from booktest import views

# ''
# index
urlpatterns = [
    url(r'^index$', views.index), # 首页
    url(r'^showarg(\d+)$', views.show_arg), # 捕获参数:位置参数
    url(r'^showkwarg(?P<num>\d+)$', views.show_kwarg), # 捕获参数:关键字参数

    url(r'^login$', views.login), # 登录页面显示
    url(r'^login_check$', views.login_check), # 登录验证

    url(r'^ajax_test$', views.ajax_test), # ajax请求页面显示
    url(r'^ajax_handle$', views.ajax_handle), # ajax请求处理

    url(r'^login_ajax$', views.login_ajax), # ajax登录页面显示
    url(r'login_ajax_check$', views.login_ajax_check), # ajax登录验证

    url(r'^set_cookie$', views.set_cookie), # 设置cookie信息
    url(r'^get_cookie$', views.get_cookie), # 获取cookie信息
]