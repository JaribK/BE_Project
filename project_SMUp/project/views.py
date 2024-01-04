#3
from django.shortcuts import render
from rest_framework import generics

from .models import Users,Posts,Products,Feedbacks
from .serializers import UsersSerializers,PostsSerializers,ProductsSerializers,FeedbacksSerializers

# Create your views here.

#Users
class UsersList(generics.ListCreateAPIView):
    serializer_class = UsersSerializers

    def get_queryset(self):
        queryset = Users.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()

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

apis_data = [
    {'name_api':'Users','src':{'list':'users','index':'users/1/'}},
    {'name_api':'Posts','src':{'list':'posts','index':'posts/1/'}},
    {'name_api':'Products','src':{'list':'products','index':'products/1/'}},
    {'name_api':'Feedbacks','src':{'list':'feedbacks','index':'feedbacks/1/'}}
]

def home(req):
    context = {'apis': apis_data}
    return render(req,'indexApi.html',context)
