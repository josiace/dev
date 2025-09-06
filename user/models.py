from django.db import models

# Create your models here.
class Blog(models.Model):
    titre=models.CharField(max_length=100)
    contenus=models.TextField()
    auteur=models.CharField(max_length=100)
    mail=models.EmailField()
    def __str__(self):
        return self.titre