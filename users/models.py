from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    UserManager
)


class CustomUserManager(BaseUserManager):

    # def create_user(self, ):
    #     pass

    # def create_superuser(self, ):
    #     pass 

    def create_user(self, email, password=None, **extra_fields): # **kwargs
        
        email = self.normalize_email(email)
        # user.is_active = False
        # user.is_staff = False
        # user.is_superuser = False
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model.objects.create(email=email, **extra_fields) # create(email=email, a=1, b=2)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email address', unique=True)
    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField('active', default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)

    USERNAME_FIELD = 'email' # null=False, unique=True

    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager() # objects.create() create_user()



    #PermissionsMixin inxertin olganimiz uchun 
    # is_superuser
    # is_staff
    # groups

    
    # null = False (emaili yo'q foydalanuvhi bo'lmaslik kerak), odatda null=False 
    # unique=True (bitta email bitta foydalanuvchi) shuning uchun blank=True bo'lmaydi
    