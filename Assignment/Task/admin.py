from django.contrib import admin
# Register your models here.
from .models import Cart
# Register your models here.
@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display =('id','item')
