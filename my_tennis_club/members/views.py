from django.shortcuts import render
from .models import Member

# Create your views here.
def members(request):
    mymembers=Member.objects.all()
    context={
        'mymembers':mymembers
    }
    return  render(request,'all_members.html',context)

def details(request,id):
    mymember=Member.objects.get(id=id)
    context={
        'mymember':mymember
    }
    return render(request,'details.html',context)

def main(request):
    return render(request,'main.html')

def testing(request):
    fruits=["Mango","Apple","Cherry"]
    context={
        'fruits':fruits
    }
    return render(request,'test.html',context)

