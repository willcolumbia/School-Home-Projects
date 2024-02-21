from django.db import models
from Calendar.models import models
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    color_code = models.CharField(max_length=6)
    location = models.CharField(max_length=100)
    team_img = models.ImageField(upload_to="pictures/")
    
    class Meta:
        managed = False
        db_table = 'Event'

class SlideShow(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pictures/")