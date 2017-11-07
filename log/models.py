from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'


class LogGroup(models.Model):
    person = models.ForeignKey(Person)
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person}: {self.created_at.date()}: {self.description}'


class Temperature(models.Model):
    group = models.ForeignKey(LogGroup)
    temperature = models.FloatField()
    notes = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.temperature}'


class Nosebleed(models.Model):
    person = models.ForeignKey(Person)
    temperature = models.FloatField()
    humidity = models.PositiveIntegerField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NosebleedCondition(models.Model):
    CONDITION_CHOICES = (
        ('temperature', 'temperature'),
        ('illness', 'illness'),
        ('other', 'other'),
    )

    accident = models.ForeignKey(Nosebleed)
    type = models.CharField(max_length=128, choices=CONDITION_CHOICES)
    value = models.FloatField(null=True, blank=True)
    notes = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
