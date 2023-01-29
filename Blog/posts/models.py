from django.db import models

# Create your models here.
class Post(models.Model):
    def __str__(self):
        return  self.Post_text
    Post_text = models.TextField(max_length=500)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    def __str__(self):
        return self.choice_text

    comment = models.ForeignKey(Post, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 250)

