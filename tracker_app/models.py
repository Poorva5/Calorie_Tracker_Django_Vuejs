from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save


class MyAccountManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("User must enter Email Address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    username = None
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class MealType(models.Model):

     MEALS_CHOICES = (
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('snacks', 'snacks'),
        ('dinner', 'dinner'),
        ('dessert', 'dessert'),
     )

     meal_name = models.CharField(max_length=10, choices=MEALS_CHOICES)

     def __str__(self):
         return self.meal_name


class FoodList(models.Model):

    food_name = models.CharField(max_length=100)
    meal_type = models.ManyToManyField(MealType)
    calorie = models.DecimalField(max_digits=5, default=0, decimal_places=2)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_eaten = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.food_name


class Profile(models.Model):

    userName = models.OneToOneField(UserData, on_delete=models.CASCADE, null=True)
    daily_calories = models.IntegerField(null=True)
    goal_weight = models.FloatField(null=True)

    def __str__(self):
        return str(self.userName.name)

    def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        else:
            pass


class Weight(models.Model):
    userName = models.ForeignKey(Profile, on_delete=models.CASCADE)
    weight = models.FloatField()
    date_recorded = models.DateField(auto_now_add=True)

















