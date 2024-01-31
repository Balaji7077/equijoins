from django.shortcuts import render

# Create your views here.
from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all() 
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='CHICAGO')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__lt=1000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(sal__gt=2500)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__lt=1000)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__gt=1000)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[:5:]
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(job='MANAGER')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__startswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__endswith='S')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__contains='ALLEN')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(ename__regex=r'SC')
    

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)