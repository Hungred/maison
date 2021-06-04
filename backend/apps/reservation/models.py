import datetime

from django.db import models


def increment_wait_number():
  last_wait = Wt.objects.all().order_by('wid').last()
  if not last_wait:
    return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000001'
  else:
      last_date = int(last_wait.wid[0:8])
      cur_date = int(str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2))
      if last_date != cur_date:
        return str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2) + '000001'
  wid = last_wait.wid
  wait_int = int(wid[8:14])
  new_wait_int = wait_int + 1
  new_wait_id = str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + str(datetime.date.today().day).zfill(2)+ str(new_wait_int).zfill(6)
  return new_wait_id

# Create your models here.
class WtCheck(models.IntegerChoices):
    WAITING = 0, '等待中'
    SERVED = 1, '已帶位'


class Book(models.Model):
    serno = models.AutoField('流水號', primary_key=True)
    bookname = models.CharField('姓', max_length=2)
    booktel = models.CharField('電話號碼', max_length=10)
    bookadt = models.PositiveIntegerField('大人數量', default=0)
    bookchd = models.PositiveIntegerField('小孩數量', default=0)
    booktime = models.DateTimeField('時間')
    remark = models.TextField('備注')
    systime = models.DateTimeField('系統時間', auto_now_add=True)

    def __str__(self):
        return str(self.systime)+str(self.bookname)


class Wt(models.Model):
    serno = models.AutoField('流水號', primary_key=True)
    wid = models.CharField('侯位編號', max_length = 20, default = increment_wait_number, editable=True)
    wtname = models.CharField('姓', max_length=2)
    wtadt = models.PositiveIntegerField('大人數量', default=0)
    wtchd = models.PositiveIntegerField('小孩數量', default=0)
    wtcheck = models.IntegerField('處理狀態', choices=WtCheck.choices)

    def __str__(self):
        return str('S')+str(self.serno)+str('/W')+str(self.wid)+str('/')+str(self.wtname)