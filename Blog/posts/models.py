from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
class Post(models.Model):
    def __str__(self):
        return self.Title
    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    Title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    Post_text = models.TextField(max_length=500, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    image = models.ImageField(Title, upload_to='images', blank=True)

class Tag(models.Model):
    Title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})
    def __str__(self):
        return '{}'.format(self.Title)
class Comment(models.Model):
    def __str__(self):
        return self.choice_text

    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)

