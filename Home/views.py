from django.shortcuts import render,redirect

from .models import *

import smtplib
from .forms import MessageForm

#Email And Password

host_email='codingprac10@gmail.com'
host_password="3',>tKPdc/#2#qU!"

# Create your views here.

def home(request):
    return render(request,"index.html")

def mail(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid:
            sender_name=request.POST['name']
            sender_email=request.POST['email']
            sender_subject=request.POST['subject']
            sender_message=request.POST['message']

            with smtplib.SMTP('smtp.gmail.com',587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                
                #Email must allow Secondary Applications
                smtp.login(host_email,host_password)
                sub="Message from Personal Website: "+sender_subject
                body="Hi Apoorv Garg,\nA person who is called "+sender_name+", just visited your website and left the following Message. His name, details and other information are as follows, please get back to them As soon as possible:\nName:\t"+sender_name+"\nEmail:\t"+sender_email+"\nSubject:\t"+sender_subject+"\nmessage:\t"+sender_message
                to="garg.apoorv1098@gmail.com"
                msg=f'Subject:{sub}\n\n{body}'
                smtp.sendmail('email',to,msg)
    
    return redirect('/')