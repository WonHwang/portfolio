from django.db import models


class Profile(models.Model):
    body = models.CharField(max_length=200)

    def __str__(self):
        return self.body


class Introduction(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body


class Project(models.Model):
    title = models.CharField(max_length=200)
    period = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='%y/%d/%m', null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title