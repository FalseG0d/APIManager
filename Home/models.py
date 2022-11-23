from django.db import models


# Create your models here.

class About(models.Model):
    image=models.ImageField(upload_to="images")
    logo=models.ImageField(upload_to="images")
    favicon=models.ImageField(upload_to="images")
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    job=models.CharField(max_length=100)
    introduction=models.TextField()
    link=models.CharField(max_length=300)
    all_work=models.CharField(max_length=300)
    all_podcast=models.CharField(max_length=300)

    def __str__(self):
        return self.first_name

class Work(models.Model):
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=30)
    link=models.CharField(max_length=300)
    visible=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Paper(models.Model):
    name=models.CharField(max_length=30)
    first_word=models.CharField(max_length=10)
    abstract=models.TextField()
    link=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Count(models.Model):
    name=models.CharField(max_length=30)
    number=models.IntegerField()
    
    def __str__(self):
        return self.name

class Media(models.Model):
    image=models.ImageField(upload_to="images")
    name=models.CharField(max_length=30)
    link=models.CharField(max_length=300)
    visible=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name=models.CharField(max_length=30)
    percentage=models.IntegerField()
    color=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    name=models.CharField(max_length=50,null=True)
    abstract=models.TextField(null=True)
    link=models.CharField(max_length=300,null=True)
    visible=models.BooleanField(default=True)
    scrapable=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Link(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)
    link=models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name=models.CharField(max_length=20)
    #play_link=models.CharField(max_length=200,default='#')
    itch_link=models.CharField(max_length=200,default='#')
    image=models.CharField(max_length=200,default='#')
    description=models.TextField()
    genre=models.CharField(max_length=20)

    visible=models.BooleanField(default=True)
    scrapable=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name