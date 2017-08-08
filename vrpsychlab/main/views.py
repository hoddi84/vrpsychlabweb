from django.shortcuts import render
from main.models import MyModel, TestModel, NameModel
from django.views.generic import TemplateView
from main.mycode import ReturnJSONAsList, UltimateTest

from django.views.decorators.csrf import csrf_exempt
from main import forms

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

@csrf_exempt
def postview(request):

    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print("Validation Success")
            print("Name: " + form.cleaned_data['name'])

            namestr = form.cleaned_data['name']

            namemodel = NameModel.objects.get_or_create(name=namestr)[0]

    return render(request, 'main/postview.html', {'namelist': NameModel.objects.all()})
