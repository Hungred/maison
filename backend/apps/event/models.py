from django.db import models
import datetime
# Create your models here.

class Events(models.Model):
    eventname = models.CharField('活動名稱', max_length=50)
    on_going = models.BooleanField('是否顯示在官網', default=True)
    hyperlink = models.TextField('FB貼文連結')
    coverimage = models.ImageField('活動封面', upload_to='eventimage', blank=True, null=True, default='eventimage/default.png')