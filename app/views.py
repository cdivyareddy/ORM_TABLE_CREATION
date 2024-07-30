from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Q
from django.db.models.functions import Length

def equi_joins(request):
    LEDO=Emp.objects.select_related('Deptno').all()
    LEDO=Emp.objects.select_related('Deptno').filter(Ename='scott')
    LEDO=Emp.objects.select_related('Deptno').filter(Deptno__Deptno=10)
    LEDO=Emp.objects.select_related('Deptno').filter(Deptno__Dname='sales')
    LEDO=Emp.objects.select_related('Deptno').filter(Deptno__Deptno__in=[10,20])
    LEDO=Emp.objects.select_related('Deptno').filter(Sal__gt=1000)
    LEDO=Emp.objects.select_related('Deptno').filter(Comm__isnull=True)
    LEDO=Emp.objects.select_related('Deptno').filter(Comm__isnull=False)
    LEDO=Emp.objects.select_related('Deptno').filter(Ename__in=['smith','jhon'])
    LEDO=Emp.objects.select_related('Deptno').filter(Sal__gte=1000,Comm__isnull=False)
    LEDO=Emp.objects.select_related('Deptno').filter(Q(Sal__gte=1000)&Q(Deptno__Deptno=20))
    LEDO=Emp.objects.select_related('Deptno').filter(Deptno__Dloc__in=('chicago','newyork'))
    LEDO=Emp.objects.select_related('Deptno').filter(Ename__startswith='s')
    LEDO=Emp.objects.select_related('Deptno').filter(Ename__endswith='t')
    LEDO=Emp.objects.select_related('Deptno').filter(Ename__startswith='s',Ename__endswith='h')
    LEDO=Emp.objects.select_related('Deptno').filter(Q(Ename__contains='a') | Q(Ename__contains='s'))
    LEDO=Emp.objects.select_related('Deptno').filter(Hiredate__year=2024)
    LEDO=Emp.objects.select_related('Deptno').filter(Hiredate__day=25)
    LEDO=Emp.objects.select_related('Deptno').filter(Hiredate__day=25,Sal__gt=2000)
    LEDO=Emp.objects.select_related('Deptno').filter(Ename__gt=Length("Ename"))

    
    d={'LEDO':LEDO}
    return render(request,'equi_joins.html',d)
def emp_de_mgr(request):
    edmo=Emp.objects.select_related('Deptno','Mgr').all()
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Ename='smith')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Ename__in=['smith','jhon'])
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Sal__gte=2000)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Sal__gt=2000)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Comm__isnull=True)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Comm__isnull=False)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Dname='sales')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Dname__in=['sales','operations'])
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Dloc='newyork')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Deptno=20)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Deptno__in=[10,20])
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Dname__contains='h')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Q(Deptno__Dname__startswith='s') | Q(Deptno__Dname__endswith='h'))
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Deptno__Dname__startswith='a',Deptno__Dname__endswith='n')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Mgr__Ename__contains='s')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Mgr__Ename__isnull=True)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Mgr__Ename__isnull=False)
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Mgr__Ename__startswith='j')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Mgr__Ename__endswith='n')
    edmo=Emp.objects.select_related('Deptno','Mgr').filter(Sal__gt=1000,Sal__lt=2000)
    edmo=Emp.objects.select_related('Deptno','Mgr').all()

    d={'edmo':edmo}
    return render(request,'emp_de_mgr.html',d)