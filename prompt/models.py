from django.db import models

# Create your models here.


class Prompt(models.Model):
    parameters = models.JSONField()
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    created_at = models.DateField(auto_now=True)

class User(models.Model):
    created_at = models.DateField(auto_now=True)
    ip_address = models.CharField(max_length=39)

class Response(models.Model):
    prompt = models.OneToOneField('Prompt', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    text = models.TextField()


