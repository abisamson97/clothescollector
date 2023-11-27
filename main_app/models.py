from django.db import models
from django.urls import reverse

# Create your models here.
class Accessory(models.Model):
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Clothes(models.Model):
    type = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)
    def __str__(self):
        return self.type
    def get_absolute_url(self):
        return reverse('detail', kwargs={'c_id': self.id})
    
class Wearing(models.Model):
  date = models.DateField('Date Worn')
  event = models.CharField(max_length=100)

  clothes = models.ForeignKey(Clothes, on_delete=models.CASCADE)
  
  def __str__(self): 
    return f"For {self.event} on {self.date}"
  
  class Meta:
       ordering = ['-date']







  
