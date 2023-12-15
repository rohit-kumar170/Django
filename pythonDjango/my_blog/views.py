# from django.shortcuts import render
import datetime

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from django.template import loader


def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now
    return HttpResponse(html)  # rendering the template in HttpResponse


def index_t(request):
    a = 1
    if a:
        return HttpResponseNotFound('<h1>Page Not Found</h1>')
    else:
        return HttpResponse('<h1>Page was Found</h1>')


@require_http_methods(['GET'])
def show_deco(request):
    return HttpResponse('<h1>This is HTTP GET request</h1>')


def index_file(request):
    template = loader.get_template('index.html')
    name = {
        'student': 'Rahul',
        'Hacker':'Raj'
    }
    return HttpResponse(template.render(name))

def index_static(request):
    return render(request,'index.html')
