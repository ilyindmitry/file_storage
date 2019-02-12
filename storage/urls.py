from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^filelist/$', views.userfile_list, name='file_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
