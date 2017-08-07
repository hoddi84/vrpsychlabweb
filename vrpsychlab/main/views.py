from django.shortcuts import render
from main.models import MyModel, TestModel

# Create your views here.
def index(request):
    json_list = MyModel.objects.all()
    json_dict = {'json_test':json_list}
    return render(request, 'main/index.html', context=json_dict)

def other(request):
    number_list = TestModel.objects.all()
    number_dict = {'dict':number_list}
    return render(request, 'main/other.html', context=number_dict)
