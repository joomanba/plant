from tkinter import N
from django.conf import settings
from django.db import models
from django.utils import timezone


class Plant(models.Model):
    이름 = models.CharField(max_length=200)
    제목 = models.CharField(max_length=200, null=True)

    학명 = models.CharField(max_length=200, null=True, blank=True)
    문 = models.CharField(max_length=200, null=True, blank=True)
    강 = models.CharField(max_length=200, null=True, blank=True)
    목 = models.CharField(max_length=200, null=True, blank=True)
    원산지 = models.CharField(max_length=200, null=True, blank=True)
    분포지 = models.CharField(max_length=200, null=True, blank=True)
    서식지 = models.CharField(max_length=200, null=True, blank=True)
    크기 = models.CharField(max_length=200, null=True, blank=True)
    꽃의색깔 = models.CharField(max_length=200, null=True, blank=True)
    개화시기 = models.CharField(max_length=200, null=True, blank=True)
    생활형 = models.CharField(max_length=200, null=True, blank=True)

    설명 = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.이름


class Photo(models.Model):
    post = models.ForeignKey(Plant, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
