from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jobs/', views.list_jobs, name='jobs'),
    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'portal/login.html'
    }, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/portal/login'
    }, name='auth_logout'),
]
