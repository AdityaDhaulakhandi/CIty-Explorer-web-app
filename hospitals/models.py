from django.db import models
from django.urls import reverse
from PIL import Image

class Hospital(models.Model):
      image=models.ImageField(default='host_logo.png', upload_to='hospital_pp')
      name=models.CharField(max_length=50,default='hospital')
      location=models.CharField(max_length=50)
      facility=models.TextField(blank=True)
      contact=models.TextField(blank=True)

      def __str__(self):
          return self.name

      def get_absolute_url(self):
          return reverse("hospital-home")
    
      
      def save(self,*args, **kwargs):
          super().save(*args, **kwargs) 

          img=Image.open(self.image.path)
          if img.height> 300 or img.width>300:
              op_size=(300,300)
              img.thumbnail(op_size)
              img.save(self.image.path)   
    
      
        
      