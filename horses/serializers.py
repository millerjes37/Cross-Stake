from rest_framework import serializers
from .models import Owner, Trainer, Horse

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class HorseSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Horse
        fields = '__all__'
