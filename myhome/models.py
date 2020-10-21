from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

class RoomType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Room(models.Model):
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def serialize(self):
        return {
            'id' : self.id,
            'type' : self.type.name,
            'devices' : [device.serialize() for device in self.devices.all()]
        }

    def __str__(self):
        return f'{self.type.name}'

class DeviceType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} ({self.id})'

class Device(models.Model):
    type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='off')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='devices')

    def serialize(self):
        return {
            'id' : self.id,
            'type' : self.type.name,
            'status' : self.status,
            'room' : self.room
        }
    
    def __str__(self):
        return f'{self.type.name} ({self.id})'

