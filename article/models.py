from django.db import models
from tinymce.models import HTMLField

class Category(models.Model):
    CATEGORY = (
        (1,'Python基础'),
        (2,'数据库'),
        (3,'Django'),
        (4,'碎言碎语'),
        (5,'源码分享'),
        (6,'学无止境'),
    )
    name = models.SmallIntegerField(choices=CATEGORY,verbose_name='文章分类')

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.get_name_display()


class ArticleModel(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    content = HTMLField(verbose_name='文章内容')
    description = models.CharField(max_length=120,null=True,default=None,verbose_name='文章描述')
    image = models.ImageField(upload_to='article',null=True,default=None,verbose_name='图片')
    create_time = models.DateField(auto_now_add=True,verbose_name='创建时间')
    modify_time = models.DateField(auto_now=True,verbose_name='修改时间')
    click_count = models.IntegerField(default=0,verbose_name='点击量')
    category = models.ForeignKey(Category,verbose_name='文章类别')

    class Meta:
        verbose_name = '我的文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title