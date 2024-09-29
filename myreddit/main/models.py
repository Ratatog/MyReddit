from django.db import models

class SubsribptionManager(models.Manager):
    def get_queryset(self, user) -> models.QuerySet:
        return super().get_queryset().filter(group__members = user)
    
class NonGroupManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(group_id = None)

class Group(models.Model):
    title = models.CharField(max_length=35, verbose_name='Название', unique=True)
    description = models.CharField(max_length=200, blank=True, null=True, default=None, verbose_name='Описание')
    photo = models.ImageField(upload_to="main/group/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото')
    admin = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, verbose_name='Админ', related_name='group')
    members = models.ManyToManyField("users.User", blank=True, verbose_name="Пользователи", related_name='member')

    def __str__(self):
        return str(self.title)

class Post(models.Model):
    text = models.CharField(max_length=50, verbose_name='Текст')
    likes = models.ManyToManyField('users.User', blank=True, verbose_name='Лайки', related_name='plikes')
    group = models.ForeignKey("main.Group", on_delete=models.CASCADE, null=True, default='', verbose_name='Группа', related_name='post')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Пользователь', related_name='post')
    tags = models.CharField(max_length=300, verbose_name='Теги', null=True, blank=True, default=None)
    
    objects = models.Manager()
    subscription = SubsribptionManager()
    non_group = NonGroupManager()
    
    class Meta:
        ordering = ['-create_date']
        indexes = [
            models.Index(fields=['text', 'group', '-create_date'])
        ]
    
    def __str__(self):
        return self.text[:20]

class Image(models.Model):
    url = models.ImageField(upload_to="main/post/%Y/%m/%d/", blank=True, null=True, verbose_name='Фото')
    post = models.ForeignKey("main.Post", null=True, blank=True, on_delete=models.CASCADE, verbose_name='Картинка', related_name='img')
    
    def __str__(self):
        return str(self.url)
    
class Comment(models.Model):
    text = models.CharField(max_length=300, verbose_name='Текст')
    likes = models.ManyToManyField('users.User', blank=True, verbose_name='Лайки', related_name='clikes')
    post = models.ForeignKey("main.Post", on_delete=models.CASCADE, verbose_name='Картинка', related_name='cpost', null=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='Пользователь', related_name='comment', null=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', null=True)
    
    class Meta:
        ordering = ['-create_date']
        
    def __str__(self):
        return self.text[:20]
