from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Dloc=models.CharField(max_length=100)

class Emp(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Sal=models.DecimalField(max_digits=10,decimal_places=2)
    Comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    Hiredate=models.DateField(auto_now=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    Mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)

class Salgrade(models.Model):
    grade=models.IntegerField(max_length=100)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)