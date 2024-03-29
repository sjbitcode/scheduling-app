from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
  # Examples:
  # url(r'^$', 'webapp.views.home', name='home'),
  # url(r'^blog/', include('blog.urls')),
  url(r"", include("schedule.urls", namespace = "schedule")),
  url(r'^admin/', include(admin.site.urls)),
)

handler404 = "misc.views.handler404"
handler500 = "misc.views.handler500"
