from django.contrib import admin
from .models import UserData, FoodList, Profile, MealType, Weight

admin.site.register(UserData)

admin.site.register(FoodList)

admin.site.register(MealType)

admin.site.register(Profile)

admin.site.register(Weight)

