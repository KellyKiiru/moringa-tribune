from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.news_today,name='newsToday'),
    path('archives/<past_date>/',views.past_days_news),
    path('search/',views.search_results,name='search_results'),
    path('article/<int:article_id>',views.article,name='article'),
    path('new/article',views.new_article,name='new_article'),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),
    path('ajax/newsletter/',views.newsletter,name='newsletter'),
    path('api/merch/',views.MerchList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)