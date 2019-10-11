from django.db import models
from django.utils import timezone

# Create your models here.

class RoomType(models.Model):
    roomType = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    rentMoney = models.CharField(max_length=10)
    shortNote = models.TextField(max_length=300)

    class Meta():
        verbose_name = 'ROOM INFO'
        verbose_name_plural = 'ROOM INFO'
    def __str__(self):
        return self.roomType + ' data' + self.status

class AdminAddress(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    
    class Meta():
        verbose_name = 'ADMIN INFO'
        verbose_name_plural = 'ADMIN INFO'
    def __str__(self):
        return 'Admin Information'

class MessageData(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    class Meta():
        verbose_name = 'MESSAGE'
        verbose_name_plural = 'MESSAGES'

    def __str__(self):
        name = self.name.split(" ")[0]
        return 'Message from '+str(name)