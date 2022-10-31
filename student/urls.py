from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('student/', StudentView.as_view()),
    path('parent/', ParentView.as_view()),
    
]
