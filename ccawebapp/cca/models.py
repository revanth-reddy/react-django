from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
CELL_CHOICES = (
    ('core','CORE'),
    ('wdct', 'WDCT'),
    ('ecell','ECELL'),
    ('robo','ROBO'),
    ('rd&i','RD&I'),
    )


class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    username=models.CharField(primary_key=True,blank=False,max_length=10)
    name = models.CharField(blank=False, max_length=255)
    mobile_no = models.CharField(blank=False,max_length=10,default="")
    email = models.CharField(blank=False,max_length=30,default="")
    dp=models.ImageField(upload_to='images/',help_text='Please upload an image of less than 3 MB')
    cell=models.CharField(choices=CELL_CHOICES,max_length=6)
    year=models.IntegerField(default=0)
    post=models.CharField(max_length=60,help_text='Use Capitals!')
    def __str__(self):
        return self.name
    def publish(self):
        self.save()

# class Avatar(models.Model):
#     avatar = models.ImageField(upload_to=imgpath )
#     user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
