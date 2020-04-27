from django.db import models

# Create your models here.
class Baby(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete=models.SET_NULL,
        null=True
    )
    

    def __str__(self):
        return 'Baby: {}'.format(self.name)