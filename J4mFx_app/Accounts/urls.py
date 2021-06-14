from django.urls import path
from Accounts import views as account_views
from .views import AddFollowersView, RemoveFollowersView, UserAccountView



urlpatterns = [
	path('Register/', account_views.RegisterView, name='register'),
	path('Profile/', account_views.UpdateProfileView, name='profile'),
	path('Account/<str:username>/', UserAccountView.as_view(), name='user-account'),
	path('Profile/<int:pk>/followers/add',AddFollowersView.as_view(), name='add-follower'),
	path('Profile/<int:pk>/followers/remove',RemoveFollowersView.as_view(), name='remove-follower'),
]