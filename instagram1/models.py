from django.db import models

# Create your models here.


class Post(models.Model):
    massage = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
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