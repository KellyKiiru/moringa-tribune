from statistics import mode
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

#class Editor(models.Model):
#    first_name=models.CharField(max_length=30)
#    last_name=models.CharField(max_length=30)
#    email=models.EmailField()
#    phone_number=models.CharField(max_length=10,blank=True)
    
#    editor_list = []
    
#    def __str__(self):
#        return self.first_name
#    def save_editor(self):
#        self.save()
#    def delete_editor(self):
#        self.delete()
#    @classmethod
#    def display_editors(cls):
#        return cls.editor_list
#    class Meta:
#        ordering = ['first_name']
        
        
class tags(models.Model):
    name = models.CharField(max_length =30)
    tags_list=[]
    def __str__(self):
        return self.name
    def save_tag(self):
        self.save()
    def delete_tag(self):
        self.delete()
    @classmethod
    def display_tags(cls):
        return cls.tags_list
    class Meta:
        ordering = ['name']
        
        
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to='articles/',blank=True)
    article_list=[]
    
    def save_article(self):
        self.save()
    def delete_article(self):
        self.delete()
    @classmethod
    def display_articles(cls):
        return cls.article_list
    @classmethod
    def todays_news(cls):
        today= dt.date.today()
        news= cls.objects.filter(pub_date__date= today)
        return news
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date=date)
        return news
    @classmethod
    def search_by_title(cls,search_term):
        news=cls.objects.filter(title__icontains=search_term)
        return news
    class Meta:
        ordering = ['title']
        
class NewsLetterRecipients(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    
    
class MoringaMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)
