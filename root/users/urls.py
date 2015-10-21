from django.conf.urls import patterns, url
from views import index
urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'users/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
    url(r'^$', index, name="index"),
)
