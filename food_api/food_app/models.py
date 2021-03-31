from django.db import models
from django.core.validators import MaxValueValidator


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, help_text='Name', verbose_name='Name')
    calories = models.FloatField(default=0.0, validators=[MaxValueValidator(9999999)], null=False,
                                 help_text='Calories', verbose_name='Calories')

    def __str__(self):
        return self.name
