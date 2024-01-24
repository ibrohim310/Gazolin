from django.db import models


class Main_page(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()
    

class Service(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()


class Blog(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()


class Contact(models.Model):
    title = models.CharField(max_length = 255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"murojat {self.title}dan"
    
