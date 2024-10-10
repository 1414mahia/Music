from django.db import models

class MusicModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()  # Use EmailField for email validation
    phn_no = models.CharField(max_length=15)  # Use CharField for phone numbers
    INSTRUMENT_CHOICES = [
        ('piano', 'Piano'),
        ('guitar', 'Guitar'),
        ('flute', 'Flute')  # Corrected 'Fluter' to 'Flute'
    ]
    instrument_type= models.CharField(max_length=10, choices=INSTRUMENT_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
