from django.urls import path

urlpatterns = [
    path('<int:pk>', PostDetail.as_view()),
    path('', PostList.as_view())
]
