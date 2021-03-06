from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^hello/$','mysite.views.hello'),
    (r'^books/$','books.views.booklist'),
    (r'^polls/',include('polls.urls')),
)
