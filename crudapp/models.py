from django.db import models


# Create your models here.
class crudmodel(models.Model):
    mycrud = models.CharField(max_length= 50)

    def __str__(self):
        return self.mycrud
        