
from django.db import models
from enum import unique
from django.core.validators import MaxValueValidator, MinValueValidator


class Thing(models.Model):
    name = models.CharField(
        max_length = 30, 
        blank = False,
        unique = True,
        )
    description = models.TextField(
        max_length = 120, 
        blank = True, 
        unique = False,
    )
    quantity = models.IntegerField(
        unique = False,
        validators = [
             MinValueValidator(0),
             MaxValueValidator(100)                   
                                ]
    )

