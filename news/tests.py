from django.test import TestCase
from .models import Article,Editor,tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    #set up method to run before every test
    
    def setUp(self):
        self.james=Editor(first_name='James',last_name='Muriuki',email='james@moringaschool.com')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))   
    #testing the saving of editors
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
    #testing deleting editors
    def test_delete_editor(self):
        self.james.save_editor()
        new_editor=Editor(first_name='Kelly',last_name='Kiiru',email='infowithkiiru@gmail.com')
        new_editor.save_editor()
        new_editor.delete_editor()
        editors=Editor.objects.all()
        self.assertTrue(len(editors),1)
    #test for displaying editors
    def test_display_all_editors(self):
        self.assertEqual(Editor.display_editors(),Editor.editor_list)
    #test for updating editors
    def test_updating_editors(self):
        self.james.save_editor()
        new_editor=Editor(first_name='Kelly',last_name='Kiiru',email='infowithkiiru@gmail.com')
        new_editor.save_editor()
        Editor.objects.filter(first_name='James').update(first_name='Ryan')
        self.assertTrue(self.james,Editor.objects.filter(first_name='Ryan'))
        
        
    
class ArticleTestClass(TestCase):
    def setUp(self):
        self.james=Editor(first_name='James',last_name='Muriuki',email='james@moringaschool.com')
        self.james.save_editor()
        
        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()
        
        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()
        
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()    
        
    def test_instance(self):
        self.assertTrue(isinstance(self.first_article,Article))
    
    def test_get_news_by_date(self):
        test_date='2022-25-05'
        date=dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        news_by_date= Article.days_news(date)
        self.assertTrue(len(news_by_date)==0)
        
    
    def test_get_news_today(self):
        today_news= Article.today_news()
        self.assertTrue(len(today_news)>0)