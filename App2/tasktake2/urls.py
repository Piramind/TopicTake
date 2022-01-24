from django.urls import include, path
from .views import LessonListView

urlpatterns = [
    path('lessons/', LessonListView.as_view())
]
