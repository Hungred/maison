from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True #email不能重複

class Position(models.TextChoices):
    BOSS = 'B', '老闆'
    MANAGER = 'M', '管理人員'
    EMP = 'E', '一般員工'


class Employee_data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empid = models.CharField('員工編號', max_length=5, unique=True)
    empname = models.CharField('員工姓名', max_length=4)
    phonenum = models.CharField('電話號碼', max_length=10)
    position = models.CharField('職位', max_length=1, choices=Position.choices)

    def __str__(self):
        field_values = []

        field_values.append(str(self.empid))
        field_values.append(str(self.empname))
        return ' '.join(field_values)

# @receiver(post_delete, sender=Employee_data)
# def delete_tag(instance, **kwargs):
#     emps = Employee_data.objects.all()
#     for emp in emps:
#         # after Tag item deleting, book.tag is set to None
#         # so if boook's tag is null, get it's author's first tag
#         if not book.tag:
#             book.tag = book.author.tags.first()
#             book.save()
