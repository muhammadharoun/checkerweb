from django.db import models

VAR = (
    ('Yes','Yes'),
    ('No','No'),
)


class Flo_Brand(models.Model):
    main_sku = models.CharField(max_length=50)
    has_variations = models.CharField(choices=VAR, max_length=50)
    url = models.URLField(max_length = 500) 
    sku1 = models.CharField(max_length=50,blank=True, null=True)
    variation1 = models.CharField(max_length=15,blank=True, null=True)
    sku2 = models.CharField(max_length=50,blank=True, null=True)
    variation2 = models.CharField(max_length=15,blank=True, null=True)
    sku3 = models.CharField(max_length=50,blank=True, null=True)
    variation3 = models.CharField(max_length=15,blank=True, null=True)
    sku4 = models.CharField(max_length=50,blank=True, null=True)
    variation4 = models.CharField(max_length=15,blank=True, null=True)
    sku5 = models.CharField(max_length=50,blank=True, null=True)
    variation5 = models.CharField(max_length=15,blank=True, null=True)
    sku6 = models.CharField(max_length=50,blank=True, null=True)
    variation6 = models.CharField(max_length=15,blank=True, null=True)
    sku7 = models.CharField(max_length=50,blank=True, null=True)
    variation7 = models.CharField(max_length=15,blank=True, null=True)
    sku8 = models.CharField(max_length=50,blank=True, null=True)
    variation8 = models.CharField(max_length=15,blank=True, null=True)
    sku9 = models.CharField(max_length=50,blank=True, null=True)
    variation9 = models.CharField(max_length=15,blank=True, null=True)
    sku10 = models.CharField(max_length=50,blank=True, null=True)
    variation10 = models.CharField(max_length=15,blank=True, null=True)
    sku11 = models.CharField(max_length=50,blank=True, null=True)
    variation11 = models.CharField(max_length=15,blank=True, null=True)
    sku12 = models.CharField(max_length=50,blank=True, null=True)
    variation12 = models.CharField(max_length=15,blank=True, null=True)
    sku13 = models.CharField(max_length=50,blank=True, null=True)
    variation13 = models.CharField(max_length=15,blank=True, null=True)
    sku14 = models.CharField(max_length=50,blank=True, null=True)
    variation14 = models.CharField(max_length=15,blank=True, null=True)
    sku15 = models.CharField(max_length=50,blank=True, null=True)
    variation15 = models.CharField(max_length=15,blank=True, null=True)
    def __str__(self):
        return self.main_sku

class Reverse_check(models.Model):
    sku = models.CharField(max_length=50)
    used = models.CharField(choices=VAR, max_length=5,blank=True, null=True)
    def __str__(self):
        return self.sku

class Flo_Id(models.Model):
    sku = models.CharField(max_length=50)
    flo_id = models.CharField(max_length=50)
    def __str__(self):
        return self.sku