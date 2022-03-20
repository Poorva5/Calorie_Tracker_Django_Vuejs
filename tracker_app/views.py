from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Weight
from datetime import datetime as dt
from .serializers import WeightSerializer
from rest_framework import generics


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class WeightView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class WeightCreateView(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class FoodLogViewSet(generics.ListAPIView):
    











