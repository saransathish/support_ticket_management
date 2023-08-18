from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
import uuid
from datetime import date
# Create your views here.
def main(request):
    tem = loader.get_template("main.html")
    return HttpResponse(tem.render())
def signin(request):
    tem = loader.get_template("index.html")
    return HttpResponse(tem.render({},request))
def signup(request):
    tem = loader.get_template("signup.html")
    return HttpResponse(tem.render({},request))
def redict(request):
    return redirect('signin')
def createuser(request):
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    age = request.POST['age']
    password = request.POST['pass']
    address = request.POST['address']

    load = users(username = username,firstname = fname,lastname = lname,email = email,age = age,password = password,address = address)
    load.save()
    return redirect('signin')
def login(request):
    uname = request.POST['uname']
    password = request.POST['pass']
    # return HttpResponse("welcome")
    print(uname,password)
    val = users.objects.filter(username = uname)
    if val:
        data = users.objects.get(username = uname)

        if data.password == password:
            load = loader.get_template('userticket.html')
            data = tickets.objects.filter(username = uname)
            if data:
                context = {
                    'data' : data,
                }
                return HttpResponse(load.render(context,request))

            else:
                data = [1,uname]
                context = {
                    'data' : data,
                }
                return HttpResponse(load.render(context,request))
            
        else:
            load = loader.get_template('notfound.html')
            return HttpResponse(load.render())
    else:
        load = loader.get_template('notfound.html')
        return HttpResponse(load.render())
def back(request):
    return redirect('signin')
def create(request):
    load = loader.get_template('ticket.html')
    return HttpResponse(load.render({},request))
def cancel(request):
    return redirect('/')
def create_ticket(request):
    username = request.POST['username']
    product = request.POST['product']
    # image = request.POST['productImage']
    reason = request.POST['reason']
    support = request.POST['support']
    description = request.POST['description']
    date_today = date.today()
    ticketid = str(uuid.uuid4())

    load = tickets(ticketid = ticketid,ticket_date =date_today, username = username,product =product,reason =reason,support = support,description =description)
    load.save()
    return redirect('/')


    
    
    
    