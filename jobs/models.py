from django.db import models

# Create your models here.
class Job(models.Model):
    # Images
    # Creating a property (where we want to save the images) of type ImageField -> saved as data, gonna accept JPG etc
    image = models.ImageField(upload_to='images/')
    # Summary
    # (how big I want this charFiled to be)
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary


