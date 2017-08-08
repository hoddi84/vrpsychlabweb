from django.shortcuts import render
from main.models import MyModel, TestModel
from django.views.generic import TemplateView
from main.mycode import ReturnJSONAsList, UltimateTest

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
