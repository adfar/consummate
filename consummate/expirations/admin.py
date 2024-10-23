from django.contrib import admin

from expirations.models import Expiration, Food

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass

@admin.register(Expiration)
class ExpirationAdmin(admin.ModelAdmin):
    pass

