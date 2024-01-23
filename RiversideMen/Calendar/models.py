from django.db import models
from django.urls import reverse
from django.utils.html import format_html
# Create your models here.
#Used to add event to Calendar
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    color_code = models.CharField(max_length=6)
    location = models.CharField(max_length=100)
    team_img = models.ImageField(upload_to="pictures/")
    
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return format_html(
            '<span style="color: {};">{}</span>',
            self.color_code,
            self.title,
        )