from django.urls import path
from mainapp import views

urlpatterns = [
    path('post/', views.PostView.as_view()),
    path('post/create/', views.PostCreateView.as_view()),
    path('post/list/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view()),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view()),
]
