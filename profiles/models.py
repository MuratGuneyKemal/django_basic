from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password = None):
            """New User Profile Creator"""
            if not email:
                raise ValueError('Email Address is needed')

            email = self.normalize_email(email=email)
            user = self.model(email=email, name=name)

            user.set_password(password) # use function since pw is sensitive info
            user.save(using=self.db)

            return user

    def create_superuser(self, email, name, password):
        """New Superuser (admin)"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True) #pk
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() # for django

    USERNAME_FIELD = 'email' # for django
    REQUIRED_FIELDS = ['name'] # for django

    # for django
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return str representation of user"""
        return self.email