from django.db.models import query
from mainapp import serializers
from mainapp.models import Post
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from mainapp.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, PostUpdateSerializer
from mainapp.pagination import StandardResultsSetPagination
from mainapp.filters import PostFilter
from mainapp.permissions import IsAuth, IsOwner


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
    filter_backend = (DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = [IsAuth]


class PostDetailView(generics.RetrieveAPIView):

    #queryset = Post.objects.filter(is_active=True)
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])


class PostCreateView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = [IsAuth]

    def perform_create(self, serializer):
        # from CreatModelMixin
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class PostUpdateView(generics.UpdateAPIView):

    #queryset = Post.objects.filter(is_active=True)
    serializer_class = PostUpdateSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])

    def get(self, request, pk):
        post_object = Post.objects.filter(is_active=True, pk=pk).first()
        serializer = PostDetailSerializer(post_object)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDeleteView(generics.DestroyAPIView):

    permission_classes = [IsOwner]

    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)