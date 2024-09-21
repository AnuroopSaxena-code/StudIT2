from django.urls import path
from .views import home, login_view, signup_view, dashboard_view, logout_view, leaderboard_view, friends_view, accept_friend_request, send_friend_request, decline_friend_request, session_hub
from .views import send_message, message_view
urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),  
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('sessionhub/', session_hub, name='session_hub'),
    path('send_request/<str:username>/', send_friend_request, name='send_friend_request'),
    path('accept_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('decline_request/<int:request_id>/', decline_friend_request, name='decline_friend_request'),
    path('friends/', friends_view, name='friends'),  # This is the URL for the friends page
    path('send_message/', send_message, name='send_message'),
    path('messages/', message_view, name='message_view'),
]
