from multiprocessing import context
from django.shortcuts import render
import json 
from .models import Tester
from .filters import TesterFilter
# Create your views here.


def index(request):
    if request.method == "POST":
            file = request.FILES['jsonfile']
            file2= request.FILES['videofile']
            # do some parsing and create the object here
            try:
                print('im here')
                data=(file.read())
                print(data)
                test=json.loads(data)
                print('im here not here')
                test['video_file']=file2
                U=Tester(**test)
                U.save() 
            except ValueError:
                print('decoding failed')
            
    

    return render(request,'index.html')

def detailview(request):
    testers=Tester.objects.all()
    #testers=Tester.objects.filter()
    testerfilter=TesterFilter(request.GET,queryset=testers)
    testers=testerfilter.qs
    context={'Testersdata':testers,'testerfilter':testerfilter}
    return render(request,'detailview.html',context)
     





