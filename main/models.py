from django.db import models


class Profile(models.Model):
    employee_id = models.CharField(max_length=4, blank=True, unique=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    middle_name = models.CharField(max_length=50, default='')
    department = models.CharField(max_length=75, default='')
    project = models.CharField(max_length=75, blank=True, default='')
    company = models.CharField(max_length=75, default='')
    schedule = models.CharField(max_length=5, default='')
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=True)

    face_data1 = models.BinaryField()
    face_data2 = models.BinaryField()
    face_data3 = models.BinaryField()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    owner = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.employee_id