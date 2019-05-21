from django.db import models


class Thread(models.Model):
    title = models.CharField(max_length=50)


class Post(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
