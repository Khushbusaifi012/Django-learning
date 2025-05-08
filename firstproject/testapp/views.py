from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):   #first view
    print(type(request))
    s="<h1> Welcome to Django Classes!! </h1>"
    return HttpResponse(s)

def time(request):    #second view
    time=datetime.datetime.now()
    k="<h1> Hello Current Date and Time is :"+str(time)+'</h1>'    #to show a time
    return HttpResponse(k)    

def html(request):   #third view
    h="<h1>This is HTML Page.</h1>"
    return HttpResponse(h)

def datetime_info(request):   #fourth view
    date=datetime.datetime.now()
    h=int(date.strftime('%H'))
    msg="<h1>Hello guyzzz</h1>"

    if(h<12):
        msg=msg+'Good Morning'
    elif(h<16):
        msg=msg+'Good Afternoon'
    elif(h<21):
        msg=msg+'Good Evening'
    else:
        msg=msg+'Good Night'
    msg=msg+'</h1><hr>'
    msg=msg+'<h1> Now Server Date and Time is:'+str(date) +'</h1>'   
    print(msg)
    return HttpResponse(msg)

def index(request):   #fifth view
    time=datetime.datetime.now()
    name='Django'
    prerequisite='Python'
    my_dict={'time':time,'name':name,'prerequisite':prerequisite}
    return render (request,'index.html',context=my_dict)

