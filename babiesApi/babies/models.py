from django.db import models
import datetime

# Create your models here.
class Baby(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete=models.CASCADE
    )
    

    def __str__(self):
        return 'Baby: {}'.format(self.name)