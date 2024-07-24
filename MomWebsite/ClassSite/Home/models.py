from django.db import models

class Student(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    preferredName = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    medical = models.CharField(max_length=80)
    siblings = models.CharField(max_length=80)
    tshirt = models.CharField(max_length=10)
    parentName1 = models.CharField(max_length=80)
    realtion1 = models.CharField(max_length=30)
    email1 = models.CharField(max_length=50)
    phoneNumber1 = models.CharField(max_length=10)
    
    parentName2 = models.CharField(max_length=80)
    realtion2 = models.CharField(max_length=30)
    email2 = models.CharField(max_length=50)
    phoneNumber2 = models.CharField(max_length=10)
    
    carline25 = models.BooleanField()
    carlinek1 = models.BooleanField()
    blueBus = models.BooleanField()
    redBus = models.BooleanField()
    walker = models.BooleanField()
    walkerLocation = models.CharField(max_length=30)
    Van = models.CharField(max_length=30)
    ACE = models.BooleanField()
    additional = models.CharField(max_length=100)
    
    def __str__(self):
        return '{} {}'.format(self.firstName, self.lastName) 
