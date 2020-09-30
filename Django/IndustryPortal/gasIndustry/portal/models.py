from django.db import models

# Create your models here.
class DCBILL(models.Model):
	BILLNO = models.CharField(max_length=200) #Primary Key
	DATE = models.DateField(blank=True, null=True)
	COMPANYNAME = models.CharField(max_length=200) #Primary Key. two attributes are used as primary key.
	PHONENO = models.CharField(max_length=200)
	GSTNO = models.CharField(max_length=200)
	NO_OXYEN_CYL = models.CharField(max_length=200)
	NO_NIT_CYL = models.CharField(max_length=200)
	NO_NIT_PURE = models.CharField(max_length=200)
	NO_ARGON_CYL = models.CharField(max_length=200)
	NO_DA_CYL = models.CharField(max_length=200)
	NO_LPG_CYL = models.CharField(max_length=200)
	NO_HYD_CYL = models.CharField(max_length=200)
	NO_CO2_CYL = models.CharField(max_length=200)
	NO_AMMO_CYL = models.CharField(max_length=200)
	DESCRIPTION =  models.CharField(max_length=1000)
	def __str__(self):
    		return "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.BILLNO,self.DATE,self.COMPANYNAME,self.PHONENO,
			self.GSTNO,self.NO_OXYEN_CYL,self.NO_NIT_CYL,self.NO_NIT_PURE,self.NO_ARGON_CYL,self.NO_DA_CYL,self.NO_LPG_CYL,
			self.NO_HYD_CYL,self.NO_CO2_CYL,self.NO_AMMO_CYL,self.DESCRIPTION)

class NORMALBILL(models.Model):    
	BILLNO = models.CharField(max_length=200) #Primary Key
	DATE = models.DateField(blank=True, null=True)
	COMPANYNAME = models.CharField(max_length=200) #Primary Key. two attributes are used as primary key.
	PHONENO = models.CharField(max_length=200)
	GSTNO = models.CharField(max_length=200)
	NO_OXYEN_CYL = models.CharField(max_length=200)
	NO_NIT_CYL = models.CharField(max_length=200)
	NO_NIT_PURE = models.CharField(max_length=200)
	NO_ARGON_CYL = models.CharField(max_length=200)
	NO_DA_CYL = models.CharField(max_length=200)
	NO_LPG_CYL = models.CharField(max_length=200)
	NO_HYD_CYL = models.CharField(max_length=200)
	NO_CO2_CYL = models.CharField(max_length=200)
	NO_AMMO_CYL = models.CharField(max_length=200)
	DESCRIPTION =  models.CharField(max_length=1000)
	def __str__(self):
    		return "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.BILLNO,self.DATE,self.COMPANYNAME,self.PHONENO,
			self.GSTNO,self.NO_OXYEN_CYL,self.NO_NIT_CYL,self.NO_NIT_PURE,self.NO_ARGON_CYL,self.NO_DA_CYL,self.NO_LPG_CYL,
			self.NO_HYD_CYL,self.NO_CO2_CYL,self.NO_AMMO_CYL,self.DESCRIPTION)	

class GSTBILL(models.Model):
	BILLNO = models.CharField(max_length=200) #Primary Key
	DATE = models.DateField(blank=True, null=True)
	COMPANYNAME = models.CharField(max_length=200) #Primary Key. two attributes are used as primary key.
	PHONENO = models.CharField(max_length=200)
	GSTNO = models.CharField(max_length=200)
	NO_OXYEN_CYL = models.CharField(max_length=200)
	NO_NIT_CYL = models.CharField(max_length=200)
	NO_NIT_PURE = models.CharField(max_length=200)
	NO_ARGON_CYL = models.CharField(max_length=200)
	NO_DA_CYL = models.CharField(max_length=200)
	NO_LPG_CYL = models.CharField(max_length=200)
	NO_HYD_CYL = models.CharField(max_length=200)
	NO_CO2_CYL = models.CharField(max_length=200)
	NO_AMMO_CYL = models.CharField(max_length=200)
	DESCRIPTION =  models.CharField(max_length=1000)
	def __str__(self):
    		return "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.BILLNO,self.DATE,self.COMPANYNAME,self.PHONENO,
			self.GSTNO,self.NO_OXYEN_CYL,self.NO_NIT_CYL,self.NO_NIT_PURE,self.NO_ARGON_CYL,self.NO_DA_CYL,self.NO_LPG_CYL,
			self.NO_HYD_CYL,self.NO_CO2_CYL,self.NO_AMMO_CYL,self.DESCRIPTION)	
