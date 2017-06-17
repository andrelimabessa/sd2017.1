from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.redirect_to_login),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', views.post_list),
    url(r'^user/tabuleiro/$', views.post_tabuleiro),
]
