#3
from django.shortcuts import render
from rest_framework import generics

from .models import Posts,Products,Feedbacks,UserPosts
from .serializers import PostsSerializers,ProductsSerializers,FeedbacksSerializers,UserPostsSerializers

#Users
#Posts
class PostsList(generics.ListCreateAPIView):
    serializer_class = PostsSerializers

    def get_queryset(self):
        queryset = Posts.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset

class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostsSerializers
    queryset = Posts.objects.all()

#Products
class ProductsList(generics.ListCreateAPIView):
    serializer_class = ProductsSerializers

    def get_queryset(self):
        queryset = Products.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductsSerializers
    queryset = Products.objects.all()

#Feedbacks
class FeedbacksList(generics.ListCreateAPIView):
    serializer_class = FeedbacksSerializers

    def get_queryset(self):
        queryset = Feedbacks.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset

class FeedbacksDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedbacksSerializers
    queryset = Feedbacks.objects.all()

#UserPosts
class UserPostsList(generics.ListCreateAPIView):
    serializer_class = UserPostsSerializers

    def get_queryset(self):
        queryset = UserPosts.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset

class UserPostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPostsSerializers
    queryset = UserPosts.objects.all()



apis_data = [
    {'name_api':'User','src':{'list':'user','index':'user/1/'}},
    {'name_api':'Posts','src':{'list':'posts','index':'posts/1/'}},
    {'name_api':'Products','src':{'list':'products','index':'products/1/'}},
    {'name_api':'Feedbacks','src':{'list':'feedbacks','index':'feedbacks/1/'}}
]

def home(req):
    context = {'apis': apis_data}
    return render(req,'indexApi.html',context)
