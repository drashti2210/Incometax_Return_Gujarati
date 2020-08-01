from django.db import models


class UserInfo(models.Model):
	UserId=models.CharField(max_length=10,primary_key=True)
	Email=models.CharField(max_length=255)
	PAN=models.CharField(max_length=10)
	Aadhar=models.CharField(max_length=12)
	FirstName=models.CharField(max_length=255)
	LastName=models.CharField(max_length=255)
	Contact=models.CharField(max_length=10)
	UseImage=models.field_name = models.ImageField(upload_to='images/')

class User1(models.Model):
		UserId=models.CharField(max_length=10,primary_key=True)
		Password=models.CharField(max_length=8)
		#Name=models.CharField(max_length=20)
		#EmailId=models.CharField(max_length=50)
class income(models.Model):
		UserId=models.CharField(max_length=10)
		Year=models.IntegerField()
		Month=models.CharField(max_length=10)
		Gross_Salary=models.IntegerField()
		#Total_Income=models.IntegerField()
		Professional_Tax=models.IntegerField()
		Group_Ins=models.IntegerField()
		Gpf=models.IntegerField()
		Hba=models.IntegerField()
		Service_Ded=models.IntegerField()
		PLI=models.IntegerField()
		LIC=models.IntegerField()
		Trans_Allow=models.IntegerField()
		Month_Ded=models.IntegerField()
		first_half_ded=models.IntegerField()
		second_half_ded=models.IntegerField()
		DA_Diff=models.IntegerField()
		HRA_Diff=models.IntegerField()
		Trans_Exp=models.IntegerField()
		PPF=models.IntegerField()
class income_Ded(models.Model):
		UserId=models.CharField(max_length=10)
		Pro_Tax=models.IntegerField()
		Trans_Allow=models.IntegerField()
		HBA_Intr=models.IntegerField()
		Mediclaim=models.IntegerField()
		P_H_Ded=models.IntegerField()
		Donation=models.IntegerField()
		Other_Ded=models.IntegerField()
		Other_income=models.IntegerField()
		GPF_Contr=models.IntegerField()
		State_Gvt_Ins=models.IntegerField()
		Repay_HBA=models.IntegerField()
		NSC_Purchase=models.IntegerField()
		PPF=models.IntegerField()
		LIC_Prem=models.IntegerField()
		PLI_Prem=models.IntegerField()
		Edu_Fee=models.IntegerField()
		JSA=models.IntegerField()
		Infra_Bond=models.IntegerField()
		Equity_Link=models.IntegerField()
		Other_Eligible=models.IntegerField()
		Total_Ded=models.IntegerField()
		Total_Income=models.IntegerField()
		Net_Tax_income=models.IntegerField()


class Form(models.Model):
    Id = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=100,default='')
    
class Textfield(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    typ = models.CharField(max_length=50)
    Label = models.CharField(max_length=100,default='')

    form = models.ForeignKey(Form,on_delete=models.CASCADE)

class Itr21(models.Model):
	Id2=models.CharField(max_length=10)
	income=models.IntegerField()
	Year=models.IntegerField()
	Net_Tax_income=models.IntegerField()