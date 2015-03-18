from django.contrib import admin

# Register your models here.
from suave.models import Client, User, Size, Order, Tailor
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'sex')

class SizeAdmin(admin.ModelAdmin):
	list_display = ('id', 'center_back', 'chest', 'sleeve', 'inside_leg', 'bust', 'hips', 'waist')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('client', 'size', 'tailor', 'Fabric', 'details', 'delivery_option', 'sex', 'status', 'cost')

class TailorAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'rate', 'phone_number', 'address', 'specialty')

admin.site.register(Client, ClientAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tailor, TailorAdmin)