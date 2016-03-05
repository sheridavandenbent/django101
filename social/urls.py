from django.conf.urls import include, url
from social import views

urlpatterns = [
    url(r'login/', views.social_login, name='login'),
    url(r'$^',     views.index, name='index'),
    url(r'home/', views.home, name='home'),
    url(r'post/add/', views.add_post, name="add_post"),
    url(r'comment/add/', views.add_comment, name='add_comment'),
    url(r'post/delete/(?P<post_id>[0-9]+)/$',   views.delete_post, name="delete_post"),
    url(r'post/edit/(?P<post_id>[0-9]+)/$',   views.edit_post, name="edit_post"),
]