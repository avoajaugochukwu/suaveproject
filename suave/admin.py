from django.contrib import admin

# Register your models here.
from suave.models import Client, User, Order, Tailor, Fabric, Style, SizeTable
class ClientAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'sex')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('client', 'tailor', 'fabric', 'style', 'details', 'delivery_option', 'sex', 'status', 'cost', 'main_order_id', 'service_option', 'sizetable', 'date', 'soft_delete')

class TailorAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'rate', 'phone_number', 'address', 'specialty', 'approved')

class FabricAdmin(admin.ModelAdmin):
	list_display = ('name', 'cost', 'sex', 'pattern', 'image_url', 'description')

class StyleAdmin(admin.ModelAdmin):
	list_display = ('name', 'cost', 'sex', 'pattern', 'description', 'style_img')

class SizeTableAdmin(admin.ModelAdmin):
	list_display = ('size_value', 'collar', 'waist', 'hips')

admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tailor, TailorAdmin)
admin.site.register(Fabric, FabricAdmin)
admin.site.register(Style, StyleAdmin)
admin.site.register(SizeTable, SizeTableAdmin)