from django.urls import path
from .views import (ReviewListView,
                    ReviewDetailView,
                    ReviewCreateView, 
                    ReviewUpdateView,
                    ReviewDeleteView,
                    UserReviewListView
                    )
                     

urlpatterns = [
    path('Reviews/', ReviewListView.as_view(), name='reviews'),
    path('user/<str:username>/', UserReviewListView.as_view(), name='user-reviews'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review-update'),
	path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
    path('review/new/', ReviewCreateView.as_view(), name='review-new'),

] 