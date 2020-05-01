from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    actionType = models.CharField(max_length=100)
    notes = models.CharField(max_length=280)
    date = models.DateField()
    baby = models.ForeignKey(
        'babies.Baby',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return 'Event: {}'.format(self.notes)