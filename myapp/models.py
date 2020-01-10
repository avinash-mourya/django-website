from django.db import models

class users2(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name+" "+self.last_name