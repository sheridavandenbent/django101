from django.conf.urls import include, url
from social import views

urlpatterns = [
    url(r'login/', views.social_login, name='login'),
    url(r'$^',     views.index, name='index'),
    url(r'home/', views.home, name='home'),
    url(r'post/add/', views.add_post, name="add_post"),
]