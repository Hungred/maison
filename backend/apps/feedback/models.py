from django.db import models


class CustomerFeedback(models.Model):
    name = models.CharField('聯絡姓名', max_length=10)
    email = models.EmailField('聯絡信箱', max_length=254)
    cometime = models.DateField('光顧時間', auto_now_add=True)
    content = models.TextField('意見回饋', blank=False, max_length=500)

    def __str__(self):
        field_values = []

        field_values.append(str(self.name))
        field_values.append(str(self.cometime))
        return ' '.join(field_values)