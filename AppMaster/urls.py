
from django.urls import path
from AppMaster.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path("/", inicio, name="inicio"),
    path("exitoso/", exitoso, name="exitoso"),
    path("buscar/", buscar, name="buscar"),
    path("blog/", blog_form, name="blog"),
    path("aboutme/", aboutme, name="aboutme"),
    path("usuario/", usuario, name="usuario"),
    #path("crearuser/", crearuser, name="crearuser"),
    path("buscaruser/", register, name="buscaruser"),
    path("editarUsuario/", editarUsuario, name="editarUsuario"),
    path("editarPerfil/", editarPerfil, name='editarPerfil'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    path('usuario/list/', UsuarioList.as_view(), name='usuario_listar'),
    #path('usuario/nuevo/', UsuarioCreacion.as_view(), name='estudiante_crear'),
    path('usuario/editar/<pk>', UsuarioUpdate.as_view(), name='usuario_editar'),
    path('usuario/borrar/<pk>', UsuarioDelete.as_view(), name='usuario_borrar'),
    path('usuario/detalle/<pk>', UsuarioDetalle.as_view(), name='usuario_detalle'),    
]