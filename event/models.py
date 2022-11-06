
from django.db import models
from django.urls import reverse
from django_admin_geomap import GeoItem
from django.shortcuts import render
# from mapbox_location_field.models import LocationField

class Location(models.Model, GeoItem):
    name = models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()

    @property
    def geomap_longitude(self):
        return '' if self.lon is None else str(self.lon)

    @property
    def geomap_latitude(self):
        return '' if self.lon is None else str(self.lat)

    def __str__(self):
        return self.name


Event_Name=[
    ('River CleanUp', 'River CleanUp'),
    ('Street CleanUp', 'Street CleanUp'),
    ('Park CleanUp', 'Park CleanUp'),
    ('Blood Donation', 'Blood Donation'),
    ('Food Donation', 'Food Donation'),
    ('Money Donation', 'Money Donation'),
    ('Cloth Donation', 'Cloth Donation'),
    ('Climate Change', 'Climate Change'),
    ('Animal Rescue', 'Animal Rescue'),
    ('WildLife Conservation', 'WildLife Conservation'),
    ('Teaching', 'Teaching'),
    ('Counselling', 'Counselling')
]

class EventCategory(models.Model):
    name = models.CharField(max_length=70, choices=Event_Name)
    code = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='event_category/')
    priority = models.IntegerField(unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_user')
    # updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name +" "+ self.code
    
    def get_absolute_url(self):
        return reverse('event-category-list')

class EventSponser(models.Model):

    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='sponser/')

    def __str__(self):
        return self.name


class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    # uid = models.PositiveIntegerField(unique=True)
    description = models.TextField()    
    venue = models.ForeignKey(Location, on_delete=models.CASCADE)
    location=models.CharField(max_length=255, unique=True)
    start_time = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    sponsers = models.ManyToManyField(EventSponser)
    points = models.PositiveIntegerField()
    maximum_attende = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_created_user')
    # updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True, related_name='event_updated_user')
    created_date = models.DateField(auto_now_add=True)
    # updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('event-list')
    
    def created_updated(model, request):
        obj = model.objects.latest('pk')
        if obj.created_by is None:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()


class EventImage(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_image/')


class EventAgenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=120)
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue_name = models.CharField(max_length=255)

    def __str__(self):
        return self.speaker_name


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    attend_status_choice = (
        ('completed', 'Completed'),
        ('joined', 'Joined'),
        ('Absent', 'Absent'),
    )
    attend_status = models.CharField(choices=attend_status_choice, max_length=10)
    # created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_created_user')
    # updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_updated_user')
    # created_date = models.DateField(auto_now_add=True)
    # updated_date = models.DateField(auto_now_add=True)
    # status_choice = (
    #     ('disabled', 'Disabled'),
    #     ('active', 'Active'),
    #     ('deleted', 'Deleted'),
    #     ('blocked', 'Blocked'),
    #     ('completed', 'Completed'),
    # )
    # status = models.CharField(choices=status_choice, max_length=10)


    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('join-event-list')

    # def get_queryset(self):
    #     request = self.context.get('request', None)
    #     if request.user is not None:
    #         print(request.user)
    #         print(request.user.id)

    # def total_points(self):
    #     point= request.POST.point
    #     userList= request.POST.userList
    #     for user in userList:
    #         user=UserPoint.objects.filter(user=user)
    #         user.total_point += point
    #         user.save()

    


class EventUserWishList(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status_choice = (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(choices=status_choice, max_length=10)


    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.event)
    
    def get_absolute_url(self):
        return reverse('event-wish-list')


# class UserCoin(models.Model):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     CHOICE_GAIN_TYPE = (
#         ('event', 'Event'),
#         ('others', 'Others'),
#     )
#     gain_type = models.CharField(max_length=6, choices=CHOICE_GAIN_TYPE)
#     # event= models.ForeignKey('Event', on_delete=models.CASCADE)
#     gain_coin = models.PositiveIntegerField()
#     # created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_created_user')
#     # updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_updated_user')
#     # created_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return str(self.user)

    
class UserPoint(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE )
    uid = models.BigAutoField(primary_key=True)
    total_point = models.PositiveIntegerField()

    def __str__(self):
        return str(self.user)