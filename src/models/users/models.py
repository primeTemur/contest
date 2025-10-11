from django.db import models
from region.models import Region

class User(models.Model):
    class Meta:
        db_table = "do_users"

    firstname = models.CharField(max_length=255,)
    lastname = models.CharField(max_length=255)
    nickname = models.CharField(unique=True,max_length=255)
    birthdate = models.DateField(null=True, blank=True)
    
    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True
    )
    phone = models.CharField(max_length=20, null=True)
    locale = models.CharField(max_length=20, default="ru")
    is_superuser = models.BooleanField(default=False)
    image_id = models.PositiveIntegerField(null=True)
    email = models.EmailField(unique=True, max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

