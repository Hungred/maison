from django.db import models

class Foodtype(models.TextChoices):
    MAINDISH = 'A', '主餐'
    SIDEMEAL = 'B', '副餐'
    DESSERT = 'C', '甜點'
    DRINK = 'D', '飲料'

class Food(models.Model):
    fid = models.CharField('餐點編號', max_length=3, primary_key=True)
    foodtype = models.CharField('餐點類型', max_length=1, choices=Foodtype.choices)
    foodname = models.CharField('餐點名稱', max_length=10)
    foodprice = models.IntegerField('餐點價錢')
    foodtag = models.TextField('餐點特徵')



    def __str__(self):
        field_values = []

        field_values.append(str(self.foodname))
        field_values.append(str(self.fid))
        return ' '.join(field_values)



class Ord(models.Model):
    serno = models.AutoField(primary_key=True)
    ordtime = models.DateTimeField('日期時間', auto_now=True)
    tabnum = models.CharField('桌號', max_length=3)
    ordcheck = models.IntegerField('處理狀態', default=0)

    def __str__(self):
        field_values = []

        field_values.append(str(self.ordtime))
        field_values.append(str(self.tabnum))
        return ' '.join(field_values)

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


    foodq = models.IntegerField('數量', default=0)
    ordice = models.CharField('冰塊', max_length=3, null=True, blank=True)
    ordsua = models.CharField('甜度', max_length=3, null=True, blank=True)
    ordtip = models.TextField('備註', default='', blank=True)

    def __str__(self):
        return str(self.o_id)