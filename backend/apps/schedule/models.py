from django.db import models
from datetime import date
from django.utils import timezone


from ..login.models import Employee_data


# class Employee(models.Model):
#     empid = models.CharField('員工編號', max_length=5, primary_key=True)
#     empname = models.CharField('員工姓名', max_length=4)
#     phonenum = models.CharField('電話號碼', max_length=10)
#     position = models.CharField('職位', max_length=1, choices=Position.choices)
#     passwd = models.CharField('密碼', max_length=20)
#
#     def __str__(self):
#         field_values = []
#
#         field_values.append(str(self.empid))
#         field_values.append(str(self.empname))
#         return ' '.join(field_values)





class Job(models.TextChoices):
    # enum = value, display
    KITCHEN = 'Kitchen', '廚房'
    BAR = 'Bar', '吧台'
    INSIDE = 'Inside', '內場'
    OUTSIDE = 'Outside', '外場'
    USHER = 'Usher', '帶位'

class Worksche(models.Model):
    serno = models.AutoField('流水號', primary_key=True)
    empid = models.ForeignKey(
        Employee_data,
        on_delete=models.CASCADE, #應思考如何刪除員工但留下班表紀錄
        verbose_name='員工編號')
    workdate = models.DateField('出勤日期', auto_now=False, auto_now_add=False)
    workhour = models.CharField('出勤時', max_length=2)
    workmin = models.CharField('出勤分', max_length=2)
    offhour = models.CharField('退勤時', max_length=2)
    offmin = models.CharField('退勤分', max_length=2)
    job = models.CharField('工作崗位', max_length=10, choices=Job.choices)

    def __str__(self):
        field_values = []

        field_values.append(str(self.empid))
        field_values.append(str(self.workdate))
        field_values.append(str(self.job))
        return ' '.join(field_values)


