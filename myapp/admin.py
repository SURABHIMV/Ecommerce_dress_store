from django.contrib import admin
from .models import productt,userr,CartItem,wishlist
from django.utils.html import format_html
# Register your models here.
class product_Admin(admin.ModelAdmin):
    def image_tag(self, obj):
        if obj.image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))
        else:
            return 'No Image'
    image_tag.short_description = 'Image'
    list_display = ['product','image_tag','price','category']
admin.site.register(productt,product_Admin)

class user_Admin(admin.ModelAdmin):
    def image_tag1(self, obj):
        if obj.user_image:  # Ensure there's an image associated with the object
            return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.user_image.url))
        else:
            return 'No Image'
    image_tag1.short_description = 'Image'
    list_display = ['image_tag1','user_name','user_phone']
admin.site.register(userr,user_Admin)

class cart_Admin(admin.ModelAdmin):
    list_display = ["user", "user_name","product", "quantity","total_price"]
admin.site.register(CartItem,cart_Admin)

class wishlist_Admin(admin.ModelAdmin):
    list_display = ["user", "product", "quantity","total_price"]
admin.site.register(wishlist,wishlist_Admin)