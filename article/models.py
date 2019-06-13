# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    first_name = models.CharField('*Имя', max_length=50)
    last_name = models.CharField('*Фамилия', max_length=50)
    patronymic = models.CharField('*Отчество', max_length=50)
    email = models.EmailField('*E-mail', max_length=50)
    home = models.CharField('*Номер дома', max_length=50)
    apartment = models.CharField('*Квартира', max_length=50)
    password = models.CharField('*Пароль', max_length=100)
    contract = models.CharField('*Договор Купли-Продажи', max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Contract(models.Model):
    number = models.CharField(max_length=210)

    def __str__(self):
        return self.number


class Documents(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE,)
    name = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.name