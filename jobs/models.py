from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=300)
    project_url = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
