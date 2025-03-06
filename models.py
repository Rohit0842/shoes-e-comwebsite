from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


# Product model to store product details
class product(models.Model):
    product_id = models.IntegerField(primary_key=True,)  # Make this the primary key
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=100)
    product_date = models.DateField()
    image = models.ImageField(upload_to="static/images", default="default.jpg")
    slug = models.SlugField(default="", null="false")
    def __str__(self):
        return str(self.product_id)  


# LastNameModel stores a last name (not used anywhere else in the code)
class LastNameModel(models.Model):
    last_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.last_name


# Profile model which is linked to the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    def __str__(self):
        return self.user.username  # assuming you want the username here


# Custom adapter for social login (optional, you can extend if needed)
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, data=None):
        user = super().save_user(request, sociallogin, data)
        # Add additional logic if needed
        return user


# Function to manually create a profile for a user (not needed if using signals)
def create_profile(user):
    profile = Profile.objects.create(user=user)
    return profile

