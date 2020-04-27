from django.db import models

# Create your models here.
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    

    def __str__(self):
        return 'Baby: {}'.format(self.name)