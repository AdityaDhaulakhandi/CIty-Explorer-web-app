from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

class Business(models.Model):
      owner= models.ForeignKey(User, on_delete=models.CASCADE)
      image=models.ImageField(default='bus_logo.png', upload_to='business_pp')
      name=models.CharField(max_length=50,default='business')
      location=models.CharField(max_length=50)
      description=models.TextField(blank=True)
      contact=models.TextField(blank=True)
      link=models.TextField(blank=True)

      def __str__(self):
          return self.name

      def get_absolute_url(self):
          return reverse("business-home")
    
      
      def save(self,*args, **kwargs):
          super().save(*args, **kwargs) 

          img=Image.open(self.image.path)
          if img.height> 300 or img.width>300:
              op_size=(300,300)
              img.thumbnail(op_size)
              img.save(self.image.path)   
    
      
        
      