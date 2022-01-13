# posts/urls.py

from django.conf.urls import url

from . import views
from .views import (
    ListPostView,
    CreatePostView,
    UpdatePostView,
)

app_name = 'posts'
urlpatterns = [
    url(r'^create-posts/$', CreatePostView.as_view(), name='create-post'),
    url(r'^list-posts/$', ListPostView.as_view(), name='list-posts'),
    url(r'^update-post/(?P<pk>[-\w]+)$', UpdatePostView.as_view(), name='update-post'),
    url(r'^delete-post/(?P<pk>[-\w]+)$', views.delete_post, name='delete-post'),

]
