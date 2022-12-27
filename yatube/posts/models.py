from django.contrib.auth import get_user_model
from django.db import models

from .validators import post_text_validator as ptv

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200,)
    slug = models.SlugField(
        'Slug-группы',
        unique=True,
        blank=False,
    )
    description = models.TextField('Описание',)

    class Meta:
        verbose_name_plural = 'Сообщества'
        verbose_name = 'сообщество'
        ordering = ('title',)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField('Текст статьи', validators=[ptv],)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True,)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество',
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'cтатью'
        verbose_name_plural = 'Статьи'
        ordering = ('-pub_date',)
