from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp.serializers import PostListSerializer, PostCreateSerializer, PostDetailSerializer, PostUpdateSerializer
from mainapp.pagination import StandardResultsSetPagination
from mainapp.filters import PostFilter
from mainapp.permissions import IsAuth, IsOwner
from mainapp.models import Post


class PostView(APIView):
    """
    Display all Posts
    """

    def get(self, request):
        post_objects = Post.objects.all()
        serializer = PostListSerializer(post_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(generics.ListAPIView):
    """
    Display all Posts with is_active = True
    """

    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostListSerializer
    pagination_class = StandardResultsSetPagination
    filter_backend = (DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = [IsAuth]


class PostDetailView(generics.RetrieveAPIView):
    """
    Display post with pk
    """

    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostDetailSerializer
    permission_classes = [IsOwner]

    # def get_queryset(self):
    #    return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])


class PostCreateView(generics.CreateAPIView):
    """
    Create Post
    """

    serializer_class = PostCreateSerializer
    permission_classes = [IsAuth]

    def perform_create(self, serializer):
        # from CreateModelMixin
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class PostUpdateView(generics.UpdateAPIView):
    """
    Update Post
    """

    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostUpdateSerializer
    permission_classes = [IsOwner]

    # def get_queryset(self):
    #    return Post.objects.filter(is_active=True, pk=self.kwargs['pk'])

    def get(self, request, pk):
        post_object = Post.objects.filter(is_active=True, pk=pk).first()
        if post_object is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostDetailSerializer(post_object)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDeleteView(generics.DestroyAPIView):
    """
    Delete post
    """

    queryset = Post.objects.all()
    permission_classes = [IsOwner]

    # def get_queryset(self):
    #    return Post.objects.filter(pk=self.kwargs['pk'])

    # def delete(self, request, *args, **kwargs):
    #    return self.destroy(request, *args, **kwargs)
