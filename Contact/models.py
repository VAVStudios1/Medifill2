from django.db import models

# Create your models here.


class FeedBack(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    number = models.IntegerField()
    description = models.CharField(max_length=500)


    def __str__(self):
        return f"{self.name} - {self.email} "
