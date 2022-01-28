from django.urls import include, path
from .views import LessonListView, StudentsIView, GroupPairsView, ReportView, pupils_list, ReportViewSet, GroupViewSet, AddReport
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('lessons/', LessonListView.as_view())
#router.register('lessons/<int:pk>', StudentsIView.as_view())
#router.register('groups/<int:pk>', GroupPairsView.as_view())
#router.register('students/<int:pk>', ReportView.as_view())
#router.register('students/pupils_list', pupils_list)
#router.register('students/report', ReportViewSet)
#router.register('groups', GroupViewSet)


'''
urlpatterns = [
    path('', include(router.urls))
]

'''
urlpatterns = [
    path('lessons/', LessonListView.as_view()),
    path('lessons/<int:pk>', StudentsIView.as_view()),
    path('groups/<int:pk>', GroupPairsView.as_view()),
    path('students/pupils_list', ReportView.as_view()),
    path('students/report/', AddReport.as_view()),
]
