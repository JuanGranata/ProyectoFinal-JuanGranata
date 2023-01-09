from django.urls import path
from AppMessages.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path("", inicio, name="inicio"),
    path("exitoso/", exitoso, name="exitoso"),
    
    path('msg_list/', msg_list, name='msg_list'),
    path('msg/<int:pk>/', msg_detail, name='msg_detail'),
    path('msg_new/', msg_new, name='msg_new'),
	path('msg/<int:pk>/edit/', msg_edit, name='msg_edit'),
    path('msg/<int:pk>/delete/', msg_delete, name='msg_delete'),

]