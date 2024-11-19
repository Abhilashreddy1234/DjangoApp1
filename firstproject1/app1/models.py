from django.db import models
class member(models.Model):
    fname=models.CharField(max_length=225)
    lname=models.CharField(max_length=225)
    phone=models.CharField(max_length=15,default='0000000000')
    joined_date=models.DateField(max_length=10)
    record_id=models.IntegerField(null=True)
    def __str__(self):
        return f"{self.fname} {self.lname}"