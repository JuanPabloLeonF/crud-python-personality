from django.db import models
import uuid


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    
    identification = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    
    listCurses = models.ManyToManyField(
        'Curse'
    )
    
    
class Curse(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    
    dateCreate = models.DateField(
        auto_now_add=True,
        null=False,
        blank=False
    )
    
    dateUpdate = models.DateField(
        auto_now=True,
        null=False,
        blank=False
    )