from django.conf.urls import url
from django.urls import path, re_path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views as auth_views
from usuarios.views import RegistrarUsuarioView

urlpatterns = [
    re_path(r'^registrar$', RegistrarUsuarioView.as_view(), name='registrar'),
    re_path(r'^login$', auth_views.login, {'template_name':'login.html'}, name='login'),
    re_path(r'^logout$', auth_views.logout, {'next_page':'/'}, name='logout')
]
