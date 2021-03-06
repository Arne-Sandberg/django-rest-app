from django.db import models

class Resume(models.Model):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    age = models.PositiveIntegerField(default=0)
    email = models.CharField(max_length=100, default='')
    desired_profession = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, default=0)

    class Meta:
        ordering = ('id',)

class PastExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default='')
    company = models.CharField(max_length=50)
    dt_start = models.DateField()
    dt_end = models.DateField(default='')
    description = models.CharField(max_length=500)

    class Meta:
        ordering = ('id',)

class Address(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, default='')
    country = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)