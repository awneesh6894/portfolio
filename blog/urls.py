
from django.urls import path,include
import blog.views

urlpatterns = [

    path('',blog.views.allblogs,name='allblogs'),
    path('<int:blog_id>/',blog.views.detail,name='detail'),

]
