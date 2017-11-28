from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name="list"),
    url(r'^(?P<post_slug>[-\w]+)/$', views.PostDetailView.as_view(), name="detail"),
    url(r'^(?P<post_slug>[-\w]+)/delete/$', views.PostDeleteView.as_view(), name="delete"),

]