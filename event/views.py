from django.shortcuts import render
from rest_framework import generics,viewsets
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
import requests


from rest_framework.decorators import api_view

# Create your views here.
class LocationList(generics.ListCreateAPIView):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    filter_backends= [SearchFilter]
    search_fields= ['name']

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
    search_fields= ['status','start_date', 'venue__name', 'location']

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
    filter_backends= [SearchFilter]
    search_fields= ['user__username']


class UserEventList(generics.ListCreateAPIView):
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset=EventMember.objects.all()
    serializer_class = EventMemberSerializer
    filter_backends= [SearchFilter]
    search_fields= ['user__username', 'event__name']




    # def get_queryset(self):
    #     request = self.context.get('request', None)
    #     if request.user is not None:
    #         print(request.user)
    #         print(request.user.id)
    ######################VVVVVVVVVVVVVVVVVVVVVVVV#############
    # def get_queryset(self):
        # user = Token.objects.get.user
        # user = Token.objects.get(key='token string').user
        #----------xxxxxx------------
        # user_id = self.request.user
        # return EventMember.objects.filter(event=user_id)
    #--------------------------VVVVVVVVVVVVVVVVVVVVV------------
    # def username(self):
    #     usern = User.objects.get(id=self.user)
    #     usern = usern.username
    #     return usern

class UserEventCreatedList(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        # user_id = self.request.user
        return Event.objects.filter('created_user')


@api_view(['GET', 'POST'])
def pointHandlerApi(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        users, point = request.data['users'], request.data['point']
        # print(users, point)
        for usr in users:
            # search
            temp= UserPoint.objects.filter(user__username=usr).values() #.update(total_point=point)
            if temp:
                t = temp[0]["total_point"]
                t+=point 
                UserPoint.objects.filter(user__username=usr).update(total_point=t)
                # print(t)
                # user.total_value = t
                # user.save()
            # return sum
    return Response("Points")



# {
# "users":["shreya", "abc"],
# "point":12
# }