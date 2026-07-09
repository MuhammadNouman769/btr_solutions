from django.db import models
from apps.utils.models import BaseModel


class Team(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    linkedin_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='team_images')

    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"