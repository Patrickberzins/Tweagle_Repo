from django.db import models

class Email(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    #date_added = models.DateField('date added')

    def __str__(self):
        return self.name
