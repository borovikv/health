from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class ParameterType(models.Model):
    title = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Type(models.Model):
    title = models.CharField(max_length=256)
    parameters = models.ManyToManyField(ParameterType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Group(models.Model):
    person = models.ForeignKey(Person, related_name='groups')
    description = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.person}: {self.description}: {self.created_at.date()}'


class Event(models.Model):
    type = models.ForeignKey(Type, related_name='events')
    subject = models.ForeignKey(Person, related_name='events')
    group = models.ForeignKey(Group, null=True, blank=True, related_name='events')
    event_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.type)

    class Meta:
        ordering = ['-event_time']


class Parameter(models.Model):
    event = models.ForeignKey(Event, related_name='parameters')
    type = models.ForeignKey(ParameterType, related_name='parameters')
    value = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.type)

class Note(models.Model):
    event = models.ForeignKey(Event, related_name='names')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
