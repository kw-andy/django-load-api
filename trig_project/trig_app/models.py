from django.db import models

# Create your models here.

class Retailer(models.Model):
    retail_name = models.CharField(max_length=30)
    retail_addr = models.CharField(max_length=300, null=True)
    def __str__(self):
        return self.retail_name

class Denomination(models.Model):
    denom_name = models.CharField(max_length=1000)
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)