from django.shortcuts import render,redirect
from .models import crudmodel
from .forms import crudform
# Create your views here.


def createcrud(request):
    crudget= crudmodel.objects.all()
    crudformget = crudform()
    if request.method =='POST':
        crudformget = crudform(request.POST)
        if crudformget.is_valid():
            crudformget.save()
    return render(request, 'crud.html',{'crudget':crudget , 'crudformget':crudformget})


def deleteview(request, pk):
    cruddelete = crudmodel.objects.get(id=pk)
    cruddelete.delete()
    return redirect('createcrud')

def updateview(request, pk):
    crudupdate = crudmodel.objects.get(id=pk)
    crudupdateform = crudform(instance=crudupdate)
    if request.method == 'POST':
        crudupdateform = crudform(request.POST,instance= crudupdate)
        if crudupdateform.is_valid():
            crudupdateform.save()
            return redirect('createcrud')
    return render(request, 'crudupdate.html',{'crudupdate':crudupdate, 'crudupdateform':crudupdateform})
