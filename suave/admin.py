from django.contrib import admin

# Register your models here.
from suave.models import Client, User
class ClientAdmin(admin.ModelAdmin):
	list_display = ('user', 'sex')

admin.site.register(Client, ClientAdmin)