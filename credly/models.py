from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.shortcuts import get_object_or_404


class UserCredlyProfile(models.Model):

    user = models.ForeignKey(User, unique=True)
    access_token = models.CharField(max_length=400, null=False, blank=False)
    refresh_token = models.CharField(max_length=400, null=False, blank=False)
    token_created = models.DateTimeField(auto_now_add=True)




def save_user_token(user_id , data):
    user_credly_profile, created = UserCredlyProfile.objects.get_or_create(user_id=user_id)
    user_credly_profile.access_token = data["token"]
    user_credly_profile.refresh_token = data["refresh_token"]
    try:
        user_credly_profile.save()
    except Exception as error:
        print "Error while saving credly token"

def get_credly_access_token(user_id):

    #TODO handle if access token is expired
    try:
        user_credly_profile = get_object_or_404(UserCredlyProfile, user_id=user_id)
        return user_credly_profile.access_token
    except Exception as error:
        return None

