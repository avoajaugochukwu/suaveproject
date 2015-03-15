from django.contrib import admin

# Register your models here.
from suave.models import Client, User, Size
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'sex')

class SizeAdmin(admin.ModelAdmin):
	pass
admin.site.register(Client, ClientAdmin)
admin.site.register(Size, SizeAdmin)