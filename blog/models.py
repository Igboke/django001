from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF','Draft'
        PUBLISHED = 'PB', 'Published'
    
    objects = models.Manager()
    published_mgr = PublishedManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='date_posted')
    content = models.TextField()
    # date published, timezone.now gives the current time
    date_posted = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(default=timezone.now)
    # date actually created may or may not be saved to draft, auto_now_add = True to get the time of the object once created, in this case a post
    date_created = models.DateTimeField(auto_now_add=True)
    # date updated, auto_now updates the time
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=2,choices=Status,default=Status.DRAFT)
    
    class Meta:
        ordering = ['date_posted']
        indexes = [models.Index(fields=['date_posted']),]
    
    def get_absolute_url(self):
        return reverse('blog:post-detail',args=[self.date_posted.year, self.date_posted.month, self.date_posted.day,
 self.slug])
    
    def __str__(self):
        return self.title
    
    def save(self, *args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Comment(models.Model):
    # comment model
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body= models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


