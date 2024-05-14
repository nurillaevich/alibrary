from rest_framework import serializers
from .models import About, Team, Category, Comment, SocialMedia, Books
from account.models import User
from account.serializers import UserSerializer


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer()

    class Meta:
        model = About
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Books
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
