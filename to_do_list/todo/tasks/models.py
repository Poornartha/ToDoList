from django.db import models

# Create your models here.


class Consumer(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Task(models.Model):
    #customer = models.ForeignKey(Consumer, on_delete=models.CASCADE, null=True, default=Consumer.objects.get(id='1'))
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

