import datetime

from django.db import models
from django.utils import timezone


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name + " " + self.country + " " + self.city


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=40)
    registration_date = models.DateTimeField(default=timezone.now(), blank=True)
    region = models.ForeignKey(Region, related_name='region')

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.number


class Object(models.Model):
    person_id = models.ForeignKey(Person)
    date = models.DateTimeField(default=timezone.now(), blank=True)
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return str(self.date) + " "


class Contact(models.Model):
    a = models.ForeignKey(Person, related_name='a')
    b = models.ForeignKey(Person, related_name='b')
    time = models.DateTimeField()

    def __str__(self):
        return str(self.a) + " " + str(self.b) + " " + str(self.time)