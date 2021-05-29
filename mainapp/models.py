from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, null=True)
    text = models.TextField(verbose_name='Описание', blank=True)
    created = models.DateTimeField(verbose_name='Время добавления/обновления', auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    time = models.DateTimeField(verbose_name='Время добавления/обновления', auto_now=True)
