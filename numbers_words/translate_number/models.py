from django.db import models


class Number_word(models.Model):
    number = models.FloatField('Сумма')
    nds = models.BooleanField('НДС',default=False)
    number_sting = models.TextField('Сумма прописью',blank=True)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = 'Сумма'
        verbose_name_plural = 'Суммы'
