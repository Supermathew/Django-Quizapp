
from django.contrib import admin
from django.urls import path,include
from quiz_app import views as quiz_app_views


urlpatterns = [
    path('', quiz_app_views.index,name='index'),
    path('quiz/<int:cat_id>', quiz_app_views.question,name='question'),
    path('submit/<int:cat_id>/<int:obj_id>', quiz_app_views.submit,name='submit'),
    path('skiped/<int:cat_id>/<int:obj_id>', quiz_app_views.skiped,name='skiped'),
    path('result/<int:cat_id>', quiz_app_views.result,name='result'),




]