from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from mainapp.models import Post
from mainapp.serializers import PostListSerializer

class TestCase(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username="test_user", password="test_user_password")
        self.post1 = Post.objects.create(name="name1", text="text1", user=self.user)
        self.post2 = Post.objects.create(name="name2", text="text2", user=self.user)
        self.post3 = Post.objects.create(name="name3", text="text3", user=self.user)

    def test_get(self):
        response = self.client.get("http://localhost:8000/api/v1/post/")
        data = PostListSerializer([self.post1, self.post2, self.post3], many=True).data
        self.assertEqual(data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post_list(self):
        # заходим в систему
        self.assertTrue(self.client.login(username="test_user", password="test_user_password"))
        # делаем http запрос
        response = self.client.get("http://localhost:8000/api/v1/post/list/")
        data = PostListSerializer([self.post1, self.post2, self.post3], many=True).data

        self.assertEqual(data, response.data['results'])
        self.assertEqual(status.HTTP_200_OK, response.status_code)