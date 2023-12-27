from django.db import models
# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="myImage")
    date=models.DateTimeField(auto_now_add=True)

   # def __str__(self) -> str:
    #    return "%s%s" %(self.photo,self.date)


