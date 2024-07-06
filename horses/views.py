from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Owner, Horse
from .serializers import OwnerSerializer, HorseSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    owner = Owner.objects.create(
        user=user,
        name=data['name'],
        email=data['email'],
        phone_number=data['phone_number'],
        billing_address=data['billing_address']
    )
    return Response(OwnerSerializer(owner).data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def add_horse(request):
    data = request.data
    owner = Owner.objects.get(id=data['owner'])
    horse = Horse.objects.create(
        name=data['name'],
        owner=owner,
        trainer=data['trainer'],
        year_born=data['year_born'],
        gender=data['gender'],
        gait=data['gait'],
        selected_stakes=data['selected_stakes']
    )
    return Response(HorseSerializer(horse).data, status=status.HTTP_201_CREATED)
