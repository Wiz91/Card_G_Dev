from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, email, First_name, Last_name, contact, pin, Location, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc, and and password.
        """
        if not email:
            raise Exception('Users must have an email address')
        
        # if password!=password2:
        #         raise Exception("Password doesn't match!")

        user = self.model(
            email=self.normalize_email(email),
            First_name=First_name,
            Last_name=Last_name,
            pin=pin,
            Location=Location,
            tc=tc,
            contact=contact,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, First_name, Last_name, contact, tc, pin, Location,password=None):
        """
        Creates and saves a superuser with the given email, name, tc, and and password.
        """
       

        user = self.create_user(
            email,
            password=password,
            First_name=First_name,
            Last_name=Last_name,
            tc=tc,
            contact=contact,
            pin=pin,
            Location=Location,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




# custom user
class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Is_staff=models.BooleanField(default=False)
    tc=models.BooleanField()
    contact=models.CharField(max_length=10)
    pin=models.CharField(max_length=10,default='')
    Location=models.CharField(max_length=20,default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    Date=models.DateTimeField(auto_now_add=True)
    Time=models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['First_name','Last_name','tc','contact','pin','Location']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


#customer models
