from rest_framework import serializers
from .models import UserData, Food, MealType, Profile, Weight


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ['id', 'email', 'name', 'password']

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name'],
                                       )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MealTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealType
        fields = ['id', 'meal_name']


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['id', 'food_name', 'meal_type', 'calorie', 'quantity']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['user', 'daily_calories', 'goal_weight']


class WeightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weight
        fields = ['user', 'weight', 'date_recorded']


