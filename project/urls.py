"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings 
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from website import views 


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^base/$', 'website.views.base'),
    url(r'^services/$', 'website.views.services'),
    url(r'^young_pics/$', 'website.views.young_pics'),
    url(r'^stylish_seniors/$', 'website.views.stylish_seniors'),
    # url(r'^account_activation/$', 'website.views.account_activation'),
    url(r'^updo/$', 'website.views.updo'),
    url(r'^$', 'website.views.navbar'),

    # Django Registration Redux
    url(r'^accounts/', include('registration.backends.default.urls')),


    

    url(r'^password/change/$',
        auth_views.password_change,
        name='password_change'),

    url(r'^password/change/done/$',
        auth_views.password_change_done,
        name='password_change_done'),

    url(r'^password/reset/$',
        auth_views.password_reset,
        name='password_reset'),

    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        name='password_reset_done'),

    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        name='password_reset_complete'),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),

    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        #'document_root': settings.MEDIA_ROOT}),

    # Form URL's
    url(r'^contact_view/$', 'website.views.contact_view'),
    url(r'^message/$', 'website.views.message'),

    
    

   

]
