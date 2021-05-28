from django.db.models import query
from mainapp import serializers
from mainapp.models import Post
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, PostUpdateSerializer
from mainapp.pagination import StandardResultsSetPagination


class PostView(APIView):

    def get(self, request, format=None):
        post_objects = Post.objects.all()
        serializer = PostListSerializer(post_objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(generics.ListAPIView):
    
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination


class PostDetailView(generics.RetrieveAPIView):

    #queryset = Post.objects.filter(is_active=True)
    serializer_class = PostDetailSerializer

    def get_queryset(self):
        return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])


class PostCreateView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer


class PostUpdateView(generics.UpdateAPIView):

    #queryset = Post.objects.filter(is_active=True)
    serializer_class = PostUpdateSerializer

    def get_queryset(self):
        return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDeleteView(generics.DestroyAPIView):
    
    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)