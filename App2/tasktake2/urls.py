from django.urls import include, path
from .views import LessonListView, StudentsIView, GroupPairsView, ReportView, ReportCreateView, StudentGroupsView, ReportDeleteView, StudentTimetable
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
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
    path('groups/', StudentGroupsView.as_view()),
    path('groups/<int:pk>', GroupPairsView.as_view()),
    path('students/my_reports', ReportView.as_view()),
    path('students/create_report/', ReportCreateView.as_view()),
    path('students/delete_report/<int:pk>', ReportDeleteView.as_view()),
    path('students/timetable', StudentTimetable.as_view())

]
