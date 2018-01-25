#! /usr/bin/python
# -*- coding:utf8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=30)

# 会员信息
class Member(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    sex = models.CharField(max_length=4)