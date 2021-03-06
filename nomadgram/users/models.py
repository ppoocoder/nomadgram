from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    
    """ User Model """
    #GENDER_CHOICES 상수(constants)추가 
    GENDER_CHOICES =(
        ('male', 'Male'),
        ('feamle','Female'),
        ('not-specified','Not specified')
    )



    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    # 추가 website, bio, phone, gender
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    # # M:M 모델 
    follower = models.ManyToManyField("self")
    following = models.ManyToManyField("self")
    
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
