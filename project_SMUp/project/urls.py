#4
from django.urls import path, include
from .views import UsersList,UsersDetail,PostsList,PostsDetail,ProductsList,ProductsDetail,FeedbacksList,FeedbacksDetail
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('users/',UsersList.as_view()),
    path('users/<int:pk>/',UsersDetail.as_view()),
    path('posts/',PostsList.as_view()),
    path('posts/<int:pk>/',PostsDetail.as_view()),
    path('products/',ProductsList.as_view()),
    path('products/<int:pk>/',ProductsDetail.as_view()),
    path('feedbacks/',FeedbacksList.as_view()),
    path('feedbacks/<int:pk>/',FeedbacksDetail.as_view()),
]