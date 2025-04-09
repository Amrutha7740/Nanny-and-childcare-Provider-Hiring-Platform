from django.db import models
 
# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)
 

class tbl_category(models.Model):
    category_name = models.CharField(max_length=100)
    category_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

 
class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    place_pincode=models.IntegerField()
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
 
class tbl_adminreg(models.Model):
    name=models.CharField(max_length=30)
    contactNumber=models.IntegerField()
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
 
class tbl_subcategory(models.Model):
    subcat_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    
