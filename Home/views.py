from django.shortcuts import render,redirect

from .models import *

import smtplib
from .forms import MessageForm

# Create your views here.

def home(request):
    about=About.objects.all()[0]
    work=Work.objects.filter(visible=True)
    paper=Paper.objects.all()
    count=Count.objects.all()
    podcast=Media.objects.filter(visible=True)
    skill=Skill.objects.all()
    article=Article.objects.filter(visible=True)
    link=Link.objects.all()
    message_form=MessageForm()
    game=Game.objects.filter(visible=True)

    context={
        'about':about,
        'works':work,
        'papers':paper,
        'counter':count,
        'podcasts':podcast,
        'skills':skill,
        'blogs':article,
        'links':link,
        'message_form':message_form,
        'games':game,
    }

    return render(request,"index.html",context)