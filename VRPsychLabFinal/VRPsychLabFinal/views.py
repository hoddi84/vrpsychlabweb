from django.views.generic import TemplateView
from django.shortcuts import render

from accounts.mycode import MakeLower

######## File Stuff #########
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.core.files.storage import default_storage
from django.conf import settings
from django.core.files import File
import os

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class LiveRecordingView(TemplateView):
    template_name = 'live.html'

def ConvertFileView(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        print(filename)
        print(settings.MEDIA_ROOT)

        newfilepath = os.path.join(settings.MEDIA_ROOT, filename)
        print(newfilepath)

        f = default_storage.open(newfilepath, 'r')
        data = f.read()
        f.close()
        os.remove(newfilepath)

        newdata = MakeLower(data)

        print(newdata)

        request = HttpResponse(newdata, content_type='application/force-download')
        request['Content-Disposition'] = 'attachment; filename="file.txt"'
        return request
    return render(request, 'convert.html')
