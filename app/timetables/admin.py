from django.contrib import admin
from .models import Course

from .models import Weekday, Meal, MealOption


admin.site.register(Weekday)
admin.site.register(Meal)
admin.site.register(MealOption)
admin.site.register(Course)
