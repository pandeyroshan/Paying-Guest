from django.contrib import admin
from .models import RoomType
from .models import AdminAddress
from .models import MessageData
# Register your models here.

admin.site.site_title = 'NUH'
admin.site.site_header = 'NUH ADMIN PANEL'
admin.site.register(RoomType)
admin.site.register(AdminAddress)
admin.site.register(MessageData)