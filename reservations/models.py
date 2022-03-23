from django.db import models

# Create your models here.
from core.models import TimeStampedModel


class Reservation(TimeStampedModel):
    STATUS_PENDING = 'pending'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_CANCELED = 'canceled'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_CONFIRMED, 'Confirmed'),
        (STATUS_CANCELED, 'Canceled')
    )

    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.room} - {self.check_in}'
