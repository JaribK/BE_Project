#2
from rest_framework import serializers
from .models import Users,Posts,Products,Feedbacks

class UsersSerializers(serializers.ModelSerializer):
    class Meta :
        model = Users
        fields = ('__all__')

class PostsSerializers(serializers.ModelSerializer):
    class Meta :
        model = Posts
        fields = ('__all__')

class ProductsSerializers(serializers.ModelSerializer):
    class Meta :
        model = Products
        fields = ('__all__')

class FeedbacksSerializers(serializers.ModelSerializer):
    class Meta :
        model = Feedbacks
        fields = ('__all__')