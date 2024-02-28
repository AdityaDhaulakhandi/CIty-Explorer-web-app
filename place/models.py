from django.db import models
from django.urls import reverse
from PIL import Image
import geocoder

token='pk.eyJ1IjoiYWRpdHlhZGhhdWwiLCJhIjoiY2wzZ3k0M2h3MTNrYTNib2Y4MWpldGJiYyJ9.qqqgsAkgcrPHo3zHv1t6Lg'

class Place(models.Model):
      image=models.ImageField(default='place_logo.png', upload_to='places_pp')
      name=models.CharField(max_length=50,default='places')
      location=models.CharField(max_length=50,blank=False)
      highlight=models.TextField(blank=True)
      latitude=models.FloatField(blank=True,null=True)
      longitude=models.FloatField(blank=True,null=True)

      def __str__(self):
          return self.name

      def get_absolute_url(self):
          return reverse("places-home")
    
      def save(self,*args, **kwargs):
          g = geocoder.mapbox(self.location,key=token)
          coor = g.latlng
          self.latitude=coor[0]
          self.longitude=coor[1]
          super().save(*args, **kwargs) 
          img=Image.open(self.image.path)
          if img.height> 300 or img.width>300:
              op_size=(300,300)
              img.thumbnail(op_size)
              img.save(self.image.path)   
    
      
        
      