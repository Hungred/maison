import datetime
from django.db import models

class BOOL_CHOICES(models.TextChoices):
    YES = 'Y', '是',
    NO = 'N', '否'

def increment_wait_number():
  last_wait = Ord.objects.all().order_by('wid').last()
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

class Foodtype(models.TextChoices):
    MAINDISH = 'A', '主餐'
    SIDEMEAL = 'B', '副餐'
    DESSERT = 'C', '甜點'
    DRINK = 'D', '飲料'


class SugOpt(models.TextChoices):
    FREE = '無糖', '無糖'
    HALF = '微糖', '微糖'
    REGULAR = '正常糖', '正常糖'

class IceOpt(models.TextChoices):
    FREE = '去冰', '去冰'
    HALF = '微冰', '微冰'
    REGULAR = '正常冰', '正常冰'
class Food(models.Model):
    fid = models.CharField('餐點編號', max_length=3, primary_key=True)
    foodtype = models.CharField('餐點類型', max_length=1, choices=Foodtype.choices)
    foodname = models.CharField('餐點名稱', max_length=10)
    foodnameEng = models.CharField('餐點名稱英文', max_length=50,  default='')
    foodprice = models.IntegerField('餐點價錢')
    foodtag = models.TextField('餐點特徵')
    on_sales = models.BooleanField('是否上架', default=True)
    image = models.ImageField('餐點圖片', upload_to='foodimage', blank=True, null=True, default='foodimage/default.png')
    isIce = models.CharField('可調整冰塊', choices=BOOL_CHOICES.choices, max_length=128, default='N')
    isSug = models.CharField('可調整甜度', choices=BOOL_CHOICES.choices, max_length=128, default='N')


    def __str__(self):
        field_values = []

        field_values.append(str(self.foodname))

        return ' '.join(field_values)



class Ord(models.Model):
    serno = models.AutoField(primary_key=True)
    ordtime = models.DateTimeField('訂單時間', auto_now_add=True)
    changetime = models.DateTimeField('變更時間', auto_now=True)
    tabnum = models.CharField('桌號', max_length=3)
    ordcheck = models.IntegerField('處理狀態', default=0)
    wid = models.CharField('訂單編號', max_length=20, default=increment_wait_number, editable=True)
    total_price = models.IntegerField('總金額', default=0)
    # def __str__(self):
    #     field_values = []
    #
    #     field_values.append(str(self.ordtime))
    #     field_values.append(str(self.tabnum))
    #     return ' '.join(field_values)
    def __str__(self):
        return str('ORD')+str(self.wid)

class ordinfo(models.Model):
    serno = models.AutoField(primary_key=True)

    o_id = models.ForeignKey(
        Ord,
        on_delete=models.PROTECT,
        verbose_name='訂單編號',
        default=''
    )

    f_id = models.ForeignKey(
        Food,
        on_delete=models.PROTECT,
        verbose_name='餐點編號',
        default=''
    )
    unique_id = models.IntegerField('專屬ID',default=0)
    foodp = models.IntegerField('小結', default=0, )
    foodq = models.IntegerField('數量', default=0)
    ordice = models.CharField('冰塊', max_length=3, choices=IceOpt.choices, null=True, blank=True)
    ordsua = models.CharField('甜度', max_length=3, choices=SugOpt.choices,null=True, blank=True)
    ordtip = models.TextField('備註', default='', blank=True)


    def __str__(self):
        return str(self.o_id)