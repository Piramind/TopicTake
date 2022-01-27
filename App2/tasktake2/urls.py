from django.urls import include, path
from .views import LessonListView, StudentsIView, GroupPairsView, ReportView, create_SOTL

urlpatterns = [
    path('lessons/', LessonListView.as_view()),
    path('lessons/<int:pk>', StudentsIView.as_view()),
    path('groups/<int:pk>', GroupPairsView.as_view()),
    path('students/<int:pk>', ReportView.as_view()),
    path('students/create_sotl', create_SOTL)   
]
