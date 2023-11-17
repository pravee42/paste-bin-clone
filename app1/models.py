from django.db import models

# Create your models here.
class Codesnippet(models.Model):
    code=models.TextField(blank=False)
    datetime=models.DateTimeField(auto_now_add=True)
    category=models.CharField(max_length=100, blank=True)
    
     