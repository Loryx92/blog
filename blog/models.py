import markdown
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    '''目录'''
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title=models.CharField(max_length=70)
    body=models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    # 文字摘要
    excerpt=models.CharField(max_length=200,blank=True)

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
    # 自定义get_absolute_url方法
    # 从django.urls中导入reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
    def save(self,*args,**kwargs):
        if not self.excerpt:
            md=markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt=strip_tags(md.convert(self.body))[:54]
        super(Post,self).save(*args,**kwargs)
    class Meta:
        ordering=['-created_time','title']