from django.db import models

# Create your models here.
import jsonfield

class ImageAnnotator(models.Model):
    """PointAnnotator"""

    content = jsonfield.JSONField()
