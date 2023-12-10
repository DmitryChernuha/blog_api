from django.urls import path, include
from posts.views import PostDetail, PostList


urlpatterns = [
    path('<int:pk>', PostDetail.as_view()),
    path('', PostList.as_view()),

]
