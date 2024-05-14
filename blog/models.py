from django.db import models
from account.models import User


class SocialMedia(models.Model):
    telegram_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class About(models.Model):
    image = models.ImageField(upload_to='about/')
    description = models.TextField()
    video = models.URLField(blank=True, null=True)
    social_media = models.OneToOneField(SocialMedia, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    full_name = models.CharField(max_length=255)
    occupation = models.CharField(max_length=50)
    portfolio_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    mini_descriptions = models.TextField()
    books_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments/')
    name = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
