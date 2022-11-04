from django.shortcuts import render
from rest_framework import generics,viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import authentication, permissions


# Create your views here.
class LocationList(generics.ListCreateAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer

class EventCategoryList(generics.ListCreateAPIView):
    queryset=EventCategory.objects.all()
    serializer_class=EventCategorySerializer
    filter_backends= [SearchFilter]
    search_fields= ['name']

class EventSponserList(generics.ListCreateAPIView):
    queryset=EventSponser.objects.all()
    serializer_class=EventSponserSerializer

# class EventList(generics.ListCreateAPIView):
#     queryset=Event.objects.all()
#     serializer_class=EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class=EventSerializer
    filter_backends= [SearchFilter]
    search_fields= ['status','start_date']

class EventImageList(generics.ListCreateAPIView):
    queryset=EventImage.objects.all()
    serializer_class=EventImageSerializer

class EventAgendaList(generics.ListCreateAPIView):
    queryset=EventAgenda.objects.all()
    serializer_class=EventAgendaSerializer

class EventMemberViewSet(viewsets.ModelViewSet):
    queryset=EventMember.objects.all()
    serializer_class=EventMemberSerializer
    filter_backends= [SearchFilter]
    search_fields= ['id', 'attend_status']

class EventUserWishListList(generics.ListCreateAPIView):
    queryset=EventUserWishList.objects.all()
    serializer_class=EventUserWishListSerializer

class UserPointViewSet(viewsets.ModelViewSet):
    queryset=UserPoint.objects.all()
    serializer_class=UserPointSerializer

class UserEventList(generics.ListCreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset=EventMember.objects.all()
    serializer_class = EventMemberSerializer

    # def get_queryset(self):
    #     user_id = self.request.user
    #     return EventMember.objects.filter(event=user_id)
    def username(self):
        usern = User.objects.get(id=self.user)
        usern = usern.username
        return usern

class UserEventCreatedList(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class = EventSerializer
    

    def get_queryset(self):
        # user_id = self.request.user
        return Event.objects.filter('created_user')




    
