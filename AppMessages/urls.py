from django.urls import path
from AppMessages.views import *


urlpatterns = [
   
#----------------------------------------------------------------------------
#URLs para mensajeria
    path('all_messages/', all_messages, name='all_messages'),
    path('new_message/', new_message, name='new_message'),
    path('chat/<id>/', chat, name='chat'),
    path('chat_view/<id>/', chat_view, name='chat_view'),
    path('respond/<receiver>', respond_message, name='respond_message'),

]