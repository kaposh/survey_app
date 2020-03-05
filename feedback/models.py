from django.db import models

# Create your models here.
class Practice(models.Model):
    name_of_practice = models.CharField(max_length=20, verbose_name="Practice", help_text="Practice", default="")
    address = models.CharField(max_length=40, verbose_name="Address", help_text="Address", default="")

    def __str__(self):
        return self.name_of_practice

class YesNoQuestion(models.Model):
    question_text = models.CharField(max_length=20, verbose_name="Question text", help_text="Question text", default="")
    choice = models.BooleanField(verbose_name="Choice", help_text="Choice")

class ScaleQuestion(models.Model):
    question_text = models.CharField(max_length=20, verbose_name="Question text", help_text="Question text", default="")
    result = models.IntegerField(verbose_name="Result", help_text="Result")