from django.db import models


# Create your models here.

class profile(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHERS', 'OTHERS'),
    )

    RELIGION = (
        ('ISLAM', 'ISLAM'),
        ('HINDU', 'HINDU'),
        ('BUDDHO', 'BUDDHO'),
        ('KRISTIAN', 'KRISTIAN'),
    )

    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='prof_pic/', default='def.png')
    address = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=15)
    gender = models.CharField(choices=GENDER, max_length=8)
    religion = models.CharField(choices=RELIGION, max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.TextField(max_length=10)

    def __str__(self):
        return self.name
