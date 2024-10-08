from django.urls import path
from .views import home, login_view, signup_view, dashboard_view, logout_view, leaderboard_view, session_hub
from .views import send_message, message_view, send_message_to_user, toggle_task_complete, edit_task, delete_task, todo_list_view, add_task
from .views import friends_view, send_friend_request, accept_friend_request, decline_friend_request, session_hub_view, delete_session, profile_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),  
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('sessionhub/', session_hub, name='session_hub'),
    path('send_message/', send_message, name='send_message'),
    path('messages/', message_view, name='message_view'),
    path('send-message-to-user/<int:user_id>/', send_message_to_user, name='send_message_to_user'),
    path('todo/', todo_list_view, name='todo_list'),
    path('todo/toggle-task-complete/', toggle_task_complete, name='toggle_task_complete'),
    path('todo/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('todo/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('add-task/', add_task, name='add_task'),
    path('message/<str:username>/', send_message_to_user, name='message_user'),
    path('friends/', friends_view, name='friends'),
    path('send_friend_request/', send_friend_request, name='send_friend_request'),
    path('accept_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('decline_request/<int:request_id>/', decline_friend_request, name='decline_friend_request'),
    path('session-hub/', session_hub, name='session_hub'),
    path('delete_session/<int:session_id>/', delete_session, name='delete_session'),
    path('profile/', profile_view, name='profile'),

]
