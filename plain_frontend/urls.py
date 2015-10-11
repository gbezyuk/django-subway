from django.conf.urls import include, url, patterns
from .views import home, assignations, developers, about

urlpatterns = (
    url(r'^$', home, name='home'),
    url(r'^assignations/', assignations, name='assignations'),
    url(r'^developers/', developers, name='developers'),
    url(r'^about/', about, name='about'),
)
