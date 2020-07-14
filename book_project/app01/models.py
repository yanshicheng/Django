from django.db import models

# Create your models here.


'''
    作者表
'''


class Authors(models.Model):
    SEX_TYPE = (
        (0, '男'),
        (1, '女')
    )

    name = models.CharField(
        max_length=12,
        verbose_name='姓 名'
    )
    age = models.IntegerField(
        verbose_name='年 龄'
    )

    sex = models.CharField(
        "性 别",
        choices=SEX_TYPE,
        max_length=16,
        default=0,
    )
    autordeail = models.OneToOneField(
        to='AuthorDetail',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='详情',
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        verbose_name = verbose_name_plural = '作者'


class AuthorDetail(models.Model):
    birthday = models.DateField(
        verbose_name='生 日'
    )
    telephone = models.CharField(
        max_length=16,
        verbose_name='手机号'
    )
    addr = models.CharField(
        max_length=64,
        verbose_name='住 址'
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间'
    )

    def __str__(self):
        return self.telephone

    class Meta:
        db_table = 'AuthorDetail'
        verbose_name = verbose_name_plural = '作者详情'


'''
作者详情表
'''


class Publisher(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='名 称'
    )
    addr = models.CharField(
        max_length=64,
        verbose_name='地 址'
    )
    email = models.EmailField(
        verbose_name='邮 箱'
    )
    telephone = models.CharField(
        max_length=16,
        verbose_name='电话号'
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间'
    )

    def __str__(self):
        return self.name

    class Meta:
        # 元数据 book_publisher
        db_table = 'Publisher'
        verbose_name = verbose_name_plural = '出版社'


class Books(models.Model):
    PUBLISHER_CHOICE = (
        (1, '发行中'),
        (2, '已发行'),
    )
    title = models.CharField(
        max_length=32,
        verbose_name='书名',
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='售价',
    )
    good = models.IntegerField(

    )
    abstract = models.TextField(
        verbose_name='简介'
    )
    publisher_state = models.IntegerField(
        choices=PUBLISHER_CHOICE,
        default=2,
        verbose_name='出版社状态'
    )
    authors = models.ManyToManyField(
        to='Authors',
        verbose_name='作者',
    )
    publisher = models.ForeignKey(
        to='Publisher',
        to_field='id',
        on_delete=models.CASCADE,
        verbose_name='出版社',
    )

    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间'
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name='修改时间'
    )

    def __str__(self):
        return self.title


    class Meta:
        # 元数据 book_publisher
        db_table = 'Books'
        verbose_name = verbose_name_plural = '书籍'