from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
router.register('event',views.EventViewSet,basename='event')
router.register('totalpoints',views.UserPointViewSet,basename='points')
router.register('eventmember',views.EventMemberViewSet,basename='event member')

urlpatterns = [
    path('',include(router.urls)),
    
]

    # path('api/eventmember', views.EventMemberList.as_view()),
