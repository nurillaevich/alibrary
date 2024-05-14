from django.urls import path
from .views import BookList, AboutList, TeamList, CategoryList, CommentList, SocialMediaList

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('about/', AboutList.as_view(), name='about_list'),
    path('team/', TeamList.as_view(), name='team_list'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('comment/', CommentList.as_view(), name='comment_list'),
    path('social-media/', SocialMediaList.as_view(), name='social_media'),

]

