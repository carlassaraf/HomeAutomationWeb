from django.contrib import admin

from .models import User, DeviceType, Device, RoomType, Room

class DeviceAdmin(admin.ModelAdmin):
    fields = ('type','status','room')

class RoomAdmin(admin.ModelAdmin):
    fields = ('type',)

# Register your models here.
admin.site.register(User)
admin.site.register(DeviceType)
admin.site.register(Device, DeviceAdmin)
admin.site.register(RoomType)
admin.site.register(Room, RoomAdmin)