from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Weight
from datetime import datetime as dt
from .serializers import WeightSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_user_weight(request, id):
    today = dt.today
    profile = Profile.objects.get(id=id)

    if request.method == 'GET':
        try:
            user_weight = Weight.objects.get(id=id, date_recored=today)
            return Response({'Weight' : user_weight.weight})
        except:
            return Response({'Error': 'Weight Recorder does not exists', "weight": 0})

    if request.method == 'POST':

        if Weight.objects.filter(id=id, date_recorder=today).exists():
            user_weight = Weight.objects.get(id=id, date_recorded=today)

            serializer = WeightSerializer(user_weight, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=profile)

        else:
            serializer = WeightSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=profile)
        return Response({"message": "Updated user weight", "weight": serializer.data})









