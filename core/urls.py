from django.conf.urls import include, url
from django.contrib import admin
from filebrowser.sites import site

urlpatterns = [
    url(r'^admin/grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/', include(admin.site.urls)),
]
