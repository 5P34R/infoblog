from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    coverpic = models.ImageField(upload_to='post', blank=True)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default='draft')

    class Meta:
        ordering = ('-publish'),

    def __str__(self) -> str:
        return self.title
