from rest_framework import serializers
from .models import *

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Location
        fields = '__all__'

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= EventCategory
        fields = '__all__'

class EventSponserSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventSponser
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields = '__all__'

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventImage
        fields = '__all__'

class EventAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventAgenda
        fields = '__all__'

class EventMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventMember
        fields = '__all__'

class EventUserWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model= EventUserWishList
        fields = '__all__'

# class EventUserCreatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Event
#         fields = ('id', 'created_by')

class UserPointSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserPoint
        fields = '__all__'