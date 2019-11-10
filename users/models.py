from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Domain(models.Model):
    name = models.CharField(max_length=100, default='', verbose_name="作用域")

    class Meta:
        verbose_name = "作用域"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class User(AbstractUser):
    domain_name = models.ForeignKey(Domain, on_delete=models.DO_NOTHING, null=True, default='normal')

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username