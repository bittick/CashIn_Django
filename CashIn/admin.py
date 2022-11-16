from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'tg_nick', 'name', 'creation_date', 'account_balance']


@admin.register(Dispatcher)
class DispatcherAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'tg_nick', 'name', 'creation_date']


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'account_balance', 'creation_date']
