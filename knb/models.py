from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise TypeError('Users must have a login.')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='user-male-circle.png')
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=15, unique=True)
    wins = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    games_total = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.set_password()

    def __str__(self):
        return self.username
