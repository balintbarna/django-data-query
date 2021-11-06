from django.shortcuts import render
from django.http import HttpResponse
import requests as req
import json


def index(request):
    example1 = "curl localhost:8080/v1/search?attribute=subject&value=missing"
    example2 = "curl localhost:8080/v1/search?attribute=priority&value=high"
    examples = "Try these:<br>{};<br>{};".format(example1, example2)
    data = "data:<br>{}".format(get_data())
    return HttpResponse("<html>{}<br>{}</html>".format(examples, data))

def get_data():
    data_url = "https://raw.githubusercontent.com/mark-dessain-maersk/interview-question/v1/data.json"
    r = req.get(data_url)
    return r.text

def search(request):
    attribute = request.GET.get('attribute', '')
    value = request.GET.get('value', '')
    if not attribute or not value:
        print("search query:\n{}:{}".format(attribute, value))
        return HttpResponse(status=400)
    data_parsed = json.loads(get_data())
    if not data_parsed:
        print("parsed data:\n{}".format(data_parsed))
        return HttpResponse(status=500)
    try:
        filtered = [x for x in data_parsed if str(value).lower() in str(x[attribute]).lower()]
        return HttpResponse(json.dumps(filtered))
    except:
        return HttpResponse(status=500)
