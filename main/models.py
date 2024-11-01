from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    uploated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.title
