from django.db import models

class UploadFile(models.Model):
  timestamp = models.CharField(max_length=30)
  exname = models.CharField(max_length=10)
  name = models.CharField(max_length=100)
  typ = models.CharField(max_length=10)
  def __unicode__(self):
    return self.timestamp

# Create your models here.
