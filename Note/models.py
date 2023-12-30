from django.db import models

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey('auth.User', related_name='note', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-updated_at']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/notes/list"