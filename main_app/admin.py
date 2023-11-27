from django.contrib import admin

from .models import Clothes, Wearing, Accessory

# Register your models here
admin.site.register(Clothes)
admin.site.register(Wearing)
admin.site.register(Accessory)
