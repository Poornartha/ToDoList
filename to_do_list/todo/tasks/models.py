from django.db import models

# Create your models here.

class Consumer(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    Customer = models.ForeignKey(Consumer, default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
