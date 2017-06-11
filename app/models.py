from django.db import models
from django.utils import timezone

# Create your models here.

class Jogada(models.Model):
    autor = models.ForeignKey('auth.User', related_name="autor")
    adversario = models.ForeignKey('auth.User', related_name='adversario')
    linha = models.CharField(max_length=2)
    coluna = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)