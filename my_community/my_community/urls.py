import notifications.urls
from django.contrib import admin
# 记得引入include
from django.urls import path, include
from article.views import article_list

# 存放映射关系的列表
urlpatterns = [
    # home
    path('', article_list, name='home'),
    path('admin/', admin.site.urls),

    #django-allauth
    path('accounts/', include('allauth.urls')),
    # 新增代码，配置app的url
    path('article/', include('article.urls', namespace='article')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
    #密码重置
    path('password-reset/', include('password_reset.urls')),
    # 评论
    path('comment/', include('comment.urls', namespace='comment')),
    #消息通知
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    # notice
    path('notice/', include('notice.urls', namespace='notice')),


]