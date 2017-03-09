from django.contrib import admin

from madplan.models import Dish

class DishAdmin(admin.ModelAdmin):
	model = Dish
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Dish, DishAdmin)