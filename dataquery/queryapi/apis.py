from django.shortcuts import render
from django.http import HttpResponse
import requests as req


def index(request):
    example1 = "curl localhost:8080/v1/search?attribute=subject&value=missing"
    example2 = "curl localhost:8080/v1/search?attribute=priority&value=high"
    examples = "Try these:<br>{};<br>{};".format(example1, example2)
    data = "data:<br>{}".format(get_data())
    return HttpResponse("<html>{}<br>{}</html>".format(examples, data))

def get_data():
    data_url = "https://raw.githubusercontent.com/mark-dessain-maersk/interview-question/v1/data.json"
    r = req.get(data_url)
    print(r)
    return r.text

def search(request):
    pass