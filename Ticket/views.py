from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import *
import uuid
from datetime import date
import smtplib
import imghdr
from email.message import EmailMessage
# Create your views here.

login1 = []
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
    if True:
        uname = request.POST['uname']
        password = request.POST['pass']

        val = users.objects.filter(username = uname)
        if val:
            data = users.objects.get(username = uname)

            if data.password == password:
                login1.append(uname)
                # return loaduser(request)
                load = loader.get_template('userticket.html')
                data = Ticket.objects.filter(username = uname)
                if data:
                    context = {
                        'data' : data,
                        'uname' :uname,
                        'flag' :True
                    }
                    return HttpResponse(load.render(context,request))

                else:
                    data = [1,uname]
                    context = {
                        'data' : data,
                        'uname' :uname,
                        'flag' :False
                    }
                    return HttpResponse(load.render(context,request))
                
            else:
                load = loader.get_template('notfound.html')
                return HttpResponse(load.render())
        else:
            load = loader.get_template('notfound.html')
            return HttpResponse(load.render())
    
def loaduser(request):
    load = loader.get_template('userticket.html')
    data = Ticket.objects.filter(username = login1[-1])
    if data:
        context = {
            'data' : data,
            'uname' :login1[-1],
            'flag' :True
        }
        return HttpResponse(load.render(context,request))
    else:
        data = [1,login1[-1]]
        context = {
            'data' : data,
            'uname' :login1[-1],
            'flag' :False
        }
        return HttpResponse(load.render(context,request))
    
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
    image = request.FILES['productImage']
    reason = request.POST['reason']
    support = request.POST['support']
    description = request.POST['description']
    date_today = date.today()
    ticketid = str(uuid.uuid4())
    status = "pending"
    load = Ticket(ticketid = ticketid,ticket_date =date_today, username = username,product =product,reason =reason,support = support,description =description,status = status,image=image)
    load.save()
    return redirect('/')
    # return HttpResponseRedirect(reverse('login', kwargs={'request':request}))

def adminlog(request):
    tem = loader.get_template("adminlog.html")
    return HttpResponse(tem.render({},request))

def adminlogin(request,id):
    if id==10:
        admin_name = request.POST['adminname']
        admin_pass = request.POST['adminpass']
        if admin_name == 'admin' and admin_pass == 'admin':
            return adminpage(request,1)
        else:
            load = loader.get_template('notfound.html')
            return HttpResponse(load.render())
    else:
        return adminpage(request,id)
def adminback(request):
    return redirect('adminlog')
    
def adminpage(request,vaule):
    load = loader.get_template('adminpage.html')
    if vaule == 1:      
        data = Ticket.objects.all()
        if data:
            context = {
                'data' : data,
            }
            
    elif vaule == 2:
            val = Ticket.objects.filter(status = 'solved')
            if val:
                data = val
            else:
                data = False
            
            context = {
                'data' : data,
            }
    elif vaule == 3:
            val = Ticket.objects.filter(status = 'cancelled')
            if val:
                data = val
            else:
                data = False
            
            context = {
                'data' : data,
            }
    else:
            val = Ticket.objects.filter(status = 'pending')
            if val:
                data = val
            else:
                data = False
            
            context = {
                'data' : data,
            }
    return HttpResponse(load.render(context,request))
def navigate(request,id):
    return HttpResponseRedirect(reverse('adminlogin', kwargs={'id': id}))
def take(request,id):
    load = Ticket.objects.get(id=id)
    load.status = "cancelled"
    load.save()
    data = users.objects.get(username = load.username)
    sendmail(data.email,data.username,"cancelled")
    return  HttpResponseRedirect(reverse('adminlogin', kwargs={'id': 1}))
def action(request,id):
    load = Ticket.objects.get(id=id)
    load.status = "solved"
    load.save()
    data = users.objects.get(username = load.username)
    sendmail(data.email,data.username,"solved")
    return  HttpResponseRedirect(reverse('adminlogin', kwargs={'id': 1}))

def sendmail(Reciever_Email,username,status):
    Sender_Email = "saransathi001@gmail.com"
    Reciever_Email = "saransathi1010@gmail.com"
    Password ="dnksboczpqjhkmox"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Hello " + username
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content(f'Hello! {username} your request on our laptop store is {status} for more information check out webpage immediately thank you come again to our store for Better service') 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    return 1