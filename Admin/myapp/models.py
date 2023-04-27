from django.db import models

# Create your models here.
class MedicalCamp_event(models.Model):
    Organiser_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    Date = models.DateField()
    contact_no = models.CharField(max_length=100)
    possibilities=(('Children','Children'),("middle age",'middle age'),('old age','old age') ,('4','all'))
    For_whom = models.CharField(max_length=100,choices=possibilities)
    facilities = models.CharField(max_length=500)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.Organiser_name

class Bloodcamp_event(models.Model):
    Organisername = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.DateField()
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername

class Educational_event(models.Model):
    Organisername = models.CharField(max_length=100)
    poss=(('1','workshops'),('2','training sessions'),('3,','classes '),('4','job_mela'))
    category =models.CharField(max_length=50,choices=poss)
    Topic = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.DateField()
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername
    #Community_building_event

#Community-building events such as festivals, fairs, and cultural celebrations that promote social cohesion and a sense of belonging.

class CBEmodel(models.Model):
    Organisername = models.CharField(max_length=100)
    poss = (('1', 'festivals'), ('2', 'fairs'), ('3,', 'cultural celebrations '))
    category=models.CharField(max_length=50,choices=poss)
    topic=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.DateField()
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername


class AnimalCampModel(models.Model):
    Organisername = models.CharField(max_length=100)
    poss = (('1', 'for dogs'), ('2', ' for Goats and sheeps'), ('3,', 'for cattles '), ('4', 'for birds'),('4', 'for dogs,for Goats and sheeps,for cattles '),('4', 'for all'))
    category=models.CharField(max_length=100,choices=poss)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.DateField()
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername

class ForScribersModel(models.Model):
    Scribename = models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.TimeField()
    camp_ends_at = models.TimeField()
    date=models.DateField()
    contact = models.CharField(max_length=100)
    #full_deatails =models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Scribename
    
class ApplicantsModel(models.Model):
    name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)

    def __str__(self):
        return self.name