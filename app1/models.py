from django.db import models

# Create your models here.
class Csv_Data(models.Model):
    name = models.CharField(default="", max_length=50)
    address = models.TextField()
    email = models.EmailField(default="",max_length=40)
    m_no = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name,self.address