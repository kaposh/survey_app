from django.db import models

# Create your models here.
class Practice(models.Model):
    name_of_practice = models.CharField(max_length=20, verbose_name="Practice", help_text="Practice", default="")
    practice_id = models.CharField(max_length=20, verbose_name="Practice_id", help_text="Practice ID", default="")
    address1 = models.CharField(max_length=40, verbose_name="Address 1", help_text="Address 1", default="")
    address2 = models.CharField(max_length=40, verbose_name="Address 2", help_text="Address 2", default="")
    address3 = models.CharField(max_length=40, verbose_name="Address 3", help_text="Address 3", default="")
    def __str__(self):
        return self.name_of_practice
