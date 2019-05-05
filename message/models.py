from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    rec = models.CharField(max_length=30, default="")
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name