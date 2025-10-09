from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    nickname = models.CharField(max_length=255, unique=True)
    birthdate = models.DateField(null=True, blank=True)
    
    # region = models.CharField(
    #     max_length=50,
    #     choices=Region.choices,
    #     default=Region.TASHKENT,
    # )

    def __str__(self):
        return self.nickname
