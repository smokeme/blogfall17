from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^more/', include('posts.urls', namespace="more")),
    url(r'^googly/', include('googly.urls', namespace="googly")),
    url(r'^gitty/', include('gitty.urls', namespace="gitty")),
    url(r'^twitty/', include('twitty.urls', namespace="twitty")),

    url(r'^comments/', include('django_comments.urls')),
    url(r'^accounts/', include('allauth.urls')),

]

if settings.DEBUG:
	urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)