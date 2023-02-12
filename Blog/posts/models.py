from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Post(models.Model):
    def __str__(self):
        return self.Post_text
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    Title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    Post_text = models.TextField(max_length=500, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

class Tag(models.Model):
    Title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    def __str__(self):
        return '{}'.format(self.Title)
class Comment(models.Model):
    def __str__(self):
        return self.choice_text

    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)

