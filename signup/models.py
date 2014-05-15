from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class LoginUserManager(BaseUserManager):
    def create_user(self, username, gender, hobby, native_place, introduce, photo_path, password=None):
        if not username:
            raise ValueError('Users must have an username')
 
        user = self.model(
            username = username,
            gender = gender,
            hobby = hobby,
            native_place = native_place,
            introduce = introduce,
            photo_path = photo_path,
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, gender, hobby=None, native_place=None, introduce=None, password=None, photo_path=None):
    
        user = self.create_user(
            username = username,
            gender = gender,
            hobby = hobby,
            native_place = native_place,
            introduce = introduce,
            password = password,
            photo_path = photo_path,

        )
        user.is_staff = True
        user.is_active = True
        user.is_admin = True

class LoginUser(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True, db_index=True)
    gender = models.BooleanField(default=False)
    hobby = models.CharField(max_length=7, null=True)
    native_place = models.CharField(max_length=40, null=True)
    introduce = models.CharField(max_length=100,null=True)
    photo_path = models.FilePathField(null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['gender']
    objects = LoginUserManager()

    class Meta:
        app_label = 'signup'

class FriendRelation(models.Model):
    username = models.ForeignKey(LoginUser)
    friend = models.IntegerField()        