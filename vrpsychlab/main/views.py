from django.shortcuts import render
from main.models import MyModel, TestModel, NameModel
from django.views.generic import TemplateView
from main.mycode import ReturnJSONAsList, UltimateTest, newfile
from django.views.decorators.csrf import csrf_exempt
from main import forms

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.core.files.storage import default_storage
from django.conf import settings
import os

# Create your views here.
def index(request):
    json_list = MyModel.objects.all()
    json_dict = {'json_test':json_list}
    return render(request, 'main/index.html', context=json_dict)

def other(request):
    number_list = TestModel.objects.all()
    number_dict = {'dict':number_list}
    return render(request, 'main/other.html', context=number_dict)

def testing(request):
    context_dict = {'testdict':UltimateTest(MyModel.objects.all())}
    return render(request, 'main/testing.html', context=context_dict)

def fileview(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        print(filename)
        print(settings.MEDIA_ROOT)

        newp = os.path.join(settings.MEDIA_ROOT, filename)
        print(newp)

        f = default_storage.open(newp, 'r')
        data = f.read()
        f.close()
        print(data)

        request = HttpResponse(data, content_type='application/force-download')
        request['Content-Disposition'] = 'attachment; filename="file.txt"'
        return request
    return render(request, 'main/fileview.html')

@csrf_exempt
def postview(request):

    if request.method == 'POST':

        print("Validation Success")

        nametest = request.POST.get('name')
        othertest = request.POST.get('keytest')
        print(nametest)
        print(othertest)


        if othertest == 'austin_powers':
            namemodel = NameModel.objects.get_or_create(name=nametest)[0]
        else:
            print("Failed POST")

    return render(request, 'main/postview.html', {'namelist': NameModel.objects.all()})
