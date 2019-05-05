from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    
    lang = models.CharField(max_length=10)
    atmosphere = models.CharField(max_length=10)
    interest = models.CharField(max_length=10)
    
    email = models.CharField(max_length = 30)
    introduce = models.TextField()
    
    main_image = models.ImageField(upload_to='image/' , default='image/unknown.png')
    
    like = models.IntegerField(default = 0)
    dislike = models.IntegerField(default = 0)
    
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name