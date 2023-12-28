from django.db import models

# Create your models here.
class note(models.Model):
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/notes/list"