from django.urls import include, path
from .views import LessonListView, StudentsIView

urlpatterns = [
    path('lessons/', LessonListView.as_view()),
    path('lesson/<int:pk>', StudentsIView.as_view())
]
