from django.urls import path
from . import views
# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

app_name = 'userprofile'

urlpatterns = [
    # 用户登录
    path('login/', views.user_login, name='login'),
    # 用户退出
    path('logout/', views.user_logout, name='logout'),
    # 用户注册
    path('register/', views.user_register, name='register'),
    # 用户删除
    path('delete/<int:id>/', views.user_delete, name='delete'),
    # 用户信息
    path('edit/<int:id>/', views.profile_edit, name='edit'),
]

#添加这行
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)