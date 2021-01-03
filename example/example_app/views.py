from .models import MyData
from django.shortcuts import render, redirect


# Create your views here.
def mainpage(request):
    return render(request, "data_collector.html")


def collect_data(request):
    url_from = request.META['HTTP_REFERER']
    new_data = request.POST.get('data')
    data_name = request.POST.get('name')
    old_data = MyData.objects.get(name=data_name)
    old_data.data += (' ' + new_data)
    old_data.save()
    return redirect(url_from)
