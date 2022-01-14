from django.db import models
from django.contrib.auth import get_user_model

class Thing(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} : {self.owner}" 

