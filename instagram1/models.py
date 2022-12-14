from django.db import models
from django.conf import settings
from django.urls import reverse

from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    # 제일 안정하고 확실한 장고 User모델을 설정하는 방법
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    massage = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    photo = models.ImageField(blank=True, upload_to='instagram1S/post/%Y/%m/%d')
    # blank 의미가 있다. 태그 지정 안 할 수 있음
    tag_set = models.ManyToManyField('Tag', blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #Java tostring
    def __str__(self):
        #return f"Custom Post object({self.id})"
        return self.massage

    # def massage_length(self):
    #     return len(self.massage)
    # massage_length.short_description = "메세지 글자수"
    #

    # url reverse
    # Detail_view 구현시 반드시 적용하기 (편함)
    def get_absolute_url(self):
        return reverse('instagram1:post_detail', args=[self.pk])

    class Mata:
        ordering = ['-id']

class Comment(models.Model):
    # 1:N
    # post = models.ForeignKey(to="Post", on_delete=models.CASCADE )
    # post = models.ForeignKey(to="Instagram.Post", on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, limit_choices_to={'is_public': True}) # post_id 필드가 생성이 됩니다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name

