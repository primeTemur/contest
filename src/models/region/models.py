from django.db import models

class Region(models.Model): 
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "do_regions"

    def __str__(self):
        return self.name
