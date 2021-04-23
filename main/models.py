from django.db import models

class Terminal(models.Model):
    name = models.CharField(max_length=50)
    last_synced = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    employee_id = models.CharField(max_length=4,blank=True, unique=True)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=75,blank=True)
    company = models.CharField(max_length=75,blank=True)
    schedule = models.CharField(max_length=5,blank=True)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    face_data1 = models.BinaryField()
    face_data2 = models.BinaryField()
    face_data3 = models.BinaryField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(Terminal, on_delete=models.CASCADE,null=True)