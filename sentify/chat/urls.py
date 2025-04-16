from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.welcome_page, name='welcome_page'),
    path('conversations/', views.conversation_list, name='conversation_list'),
    path('new/', views.new_conversation, name='new_conversation'),
    path('chat/<int:conversation_id>/', views.chat_room, name='chat_room'),
    path('chat/<int:conversation_id>/send_message/', views.send_message, name='send_message'),
    path('register/', views.user_register, name='register'), 
]
