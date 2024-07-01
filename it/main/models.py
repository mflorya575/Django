from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    description = models.TextField(verbose_name='Краткое описание', max_length=500, null=True)
    text = models.TextField(verbose_name='Полный текст записи', null=True)

    thumbnail = models.ImageField(default='default.jpg',
                                  verbose_name='Изображение записи',
                                  blank=True,
                                  upload_to='images/thumbnails/',
                                  validators=[
                                      FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
                                  )

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-publish']

    def __str__(self):
        return self.title
