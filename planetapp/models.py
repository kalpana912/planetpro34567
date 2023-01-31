from django.db import models

# Create your models here.
#this model used for to make main page dynamic
class PlanetModel(models.Model):
    background_picture=models.ImageField(upload_to='media',null=True)   #for model media image u need to install pillow
    small_heading=models.CharField(max_length=50,default='Are you a tech trainer, influencer or expert?')
    
    
#model for to add cards dynamically
class InformationModel(models.Model): 
    title=models.CharField(max_length=50)
    description=models.TextField() 
    cardimage=models.ImageField(upload_to='media',null=True)
    def __str__(self):
        return self.title 

class ContactInfoModel(models.Model):
    facebook=models.URLField(max_length=500,default="https://www.facebook.com/kalpana.choudhary.777363")
    instagram=models.URLField(max_length=500,default="https://www.instagram.com/kalpana91295")
    twitter=models.URLField(max_length=500,default="https://www.twitter.com/")

class User(models.Model):
    name=models.CharField(max_length=20)
    mobileNumber=models.CharField(max_length=11)
    mail=models.EmailField(default="abc@gmail.com")
    class Meta:
        db_table='User'
    def __str__(self):
        return self.name

  



