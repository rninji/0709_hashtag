from django.db import models

# Create your models here.
class Post(models.Model):
    TYPE_CHOICES={
        ('가구','가구'),
        ('패브릭','패브릭'),
        ('홈데코/조명','홈데코/조명'),
        ('DIY/공구','DIY/공구'),
        ('가전','가전'),
        ('수납/정리','수납/정리')
    }
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/',blank=True)
    price=models.IntegerField(default=0)
    shop=models.URLField(default='')
    type=models.CharField(max_length=20,choices=TYPE_CHOICES)
    tags=models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name
