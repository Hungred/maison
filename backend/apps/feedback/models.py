from django.db import models


# Create your models here.
class Feedback(models.Model):
    orderTime = models.DateTimeField('用餐時間')
    date_submit = models.DateTimeField('提交時間', auto_now=True)
    feedback_text = models.TextField('反饋内容')

    def __str__(self):
        return str(self.orderID)
