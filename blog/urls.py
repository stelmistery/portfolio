
from django.urls import path, include
from .views import *
urlpatterns = [
    path('', allblogs, name='allblogs'),
    path('<int:blog_id>/', detail, name='detail')
]
