from django.conf.urls import url
from . import views

urlpatterns = [
    url('signup', views.signup, name='signup'),
    url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,50})',
        views.activate, name='activate'),
    url('login', views.loginUser, name='login'),
    url('logout', views.logoutUser, name='logout'),
    url('profile', views.profileUser, name='profile'),
]