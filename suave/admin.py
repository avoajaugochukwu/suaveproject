from django.contrib import admin

# Register your models here.
from suave.models import Client, User, Size, Order, Tailor, Fabric, Style
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'sex')

class SizeAdmin(admin.ModelAdmin):
	list_display = ('id', 'center_back', 'chest', 'sleeve', 'inside_leg', 'bust', 'hips', 'waist')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('client', 'size', 'tailor', 'fabric', 'details', 'delivery_option', 'sex', 'status', 'cost', 'main_order_id', 'service_option')

class TailorAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'rate', 'phone_number', 'address', 'specialty')

class FabricAdmin(admin.ModelAdmin):
	list_display = ('name', 'cost', 'sex', 'pattern')

class StyleAdmin(admin.ModelAdmin):
	list_display = ('name', 'sex', 'cost')

admin.site.register(Client, ClientAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tailor, TailorAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(Style, StyleAdmin)