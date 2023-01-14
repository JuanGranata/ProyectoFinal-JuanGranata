from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from AppMessages.views import *
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView ,LogoutView

urlpatterns = [
   
    #path("", inicio, name="inicio"),
    #path("exitoso/", exitoso, name="exitoso"),
    
    path('msg_list/', msg_list, name='msg_list'),
    path('msg/<int:pk>/', msg_detail, name='msg_detail'),
    path('msg_new/', msg_new, name='msg_new'),
	path('msg/<int:pk>/edit/', msg_edit, name='msg_edit'),
    path('msg/<int:pk>/delete/', msg_delete, name='msg_delete'),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
