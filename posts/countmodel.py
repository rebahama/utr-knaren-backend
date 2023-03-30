from django.db import models


class Calculator(models.Model):
    price = models.IntegerField(blank=False, default=25)

    class Meta:
        ordering = ['-price']

    def __str__(self):
        return f'{self.price}'