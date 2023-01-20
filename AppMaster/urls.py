from django.urls import path
from AppMaster.views import *
from django.contrib.auth.views import LogoutView 

urlpatterns = [
   
    path("", inicio, name="inicio"),
    path("exitoso/", exitoso, name="exitoso"),
    path("buscar/", buscar, name="buscar"),
    path("aboutme/", aboutme, name="aboutme"),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
        
    path("usuario/", usuario, name="usuario"),
    path('register/', register, name='register'),

    path('listarusuarios/', listarusuarios, name="listarusuarios"),
    path('detalleUsuario/<id>/', detalleUsuario, name="detalleUsuario"),
    path("buscaruser/", buscaruser, name="buscaruser"),
    path("editarUsuario/", editarUsuario, name="editarUsuario"),
    path("eliminarUsuario/<int:id>/", eliminarUsuario, name="eliminarUsuario"),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),

	path('post_list/', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post_new/', post_new.as_view(), name='post_new'),
	path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),

    # path('SuperUser/', SuperUser, name='SuperUser'),
    # path('registerSuper/', registerSuper, name='registerSuper'),
    # path('SuperUser_list/', SuperUser_list, name='SuperUser_list'),
    # path("agregarAvatarSuper/", agregarAvatarSuper, name='agregarAvatarSuper'),

]