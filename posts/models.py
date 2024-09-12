from django.db import models

# Create your models here.
class Post(models.Model):
    title: models.CharField(max_length=100,null=False,blank=False)
    description: models.TextField(null=False,blank=False)
    autor: models.CharField(max_length=100,null=False,blank=False)
    date: models.DateField()
    tags = models.ManyToManyField('Tag')
    coments = models.ManyToManyField('Coments')

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Coments(models.Model):
    autor = models.CharField(max_length=100,null=False,blank=False)
    coment = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.autor