from django.urls import path
from .views import *
urlpatterns = [
    path('', HomeView.as_view(),name = 'home'),
    path('articles/', ArticleListView.as_view(),name = 'article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(),name = 'article_detail'),
    path('create_article/', ArticleCreateView.as_view(), name='create_article'),

]