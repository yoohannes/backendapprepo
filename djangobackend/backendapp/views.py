from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import Pics, Tester, Pics, Video
from .filters import TesterFilter
import base64


def index(request):
    if request.method == "POST":
        tester_meta = request.FILES["testerjson"].read()
        pics_meta = request.FILES["picsjson"].read()
        video_meta = request.FILES["videojson"].read()
        video_file = request.FILES["videofile"]

        try:
            tester_Decoded = json.loads(tester_meta)
            U = Tester(**tester_Decoded)
            U.save()

        except ValueError:
            print("decoding failed")

        pics = json.loads(pics_meta)
        for pic in pics:

            with open(pic["image_path"], "rb") as image_file:
                pic["image"] = base64.b64encode(image_file.read())
            del pic["image_path"]

            instance1 = Pics(**pic)
            instance1.tester_id = U.tester_ID
            instance1.save()

        video = json.loads(video_meta)
        video["video_file"] = video_file
        vid_ooj = Video(**video)
        vid_ooj.tester_id = U.tester_ID

        vid_ooj.save()

        return HttpResponse("Tester data uploaded successfully")
    return render(request, "index.html")


def detailview(request):
    pictures = Pics.objects.all()
    # testers=Tester.objects.filter()
    # print(testers.filter(tester__pics__pic_num=1))
    testerfilter = TesterFilter(request.GET, queryset=pictures)
    testers = testerfilter.qs
    context = {"Testersdata": testers, "testerfilter": testerfilter}
    return render(request, "detailview.html", context)
