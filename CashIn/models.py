from django.db import models


class Dispatcher(models.Model):
    tg_id = models.CharField(max_length=20, primary_key=True)
    tg_nick = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)


class Courier(models.Model):
    tg_id = models.CharField(max_length=20, primary_key=True)
    tg_nick = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    account_balance = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}(id:{self.tg_id})'


class Operator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    account_balance = models.FloatField()
    creation_date = models.DateTimeField(auto_now_add=True)
    logs = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'
