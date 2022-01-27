from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson
from .serializers import LessonListSerializer, StudentListSerializer, ReportListSerializer
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .forms import StudentOnTheLessonForm


def create_SOTL(request):
    data = {}

    form = StudentOnTheLessonForm(request.POST or None)
    if form.is_valid():
        form.save()

    data['form'] = form
    return render(request, 'create_sotl.html', data)

class LessonListView(APIView):

	def get(self, request):
		lessons = Lesson.objects.all()
		serializer = LessonListSerializer(lessons, many=true)
		return Response(serializer.data)

# Create your views here.
class StudentsIView(APIView):
	def get(self, request, pk):
		studento_ids = list(StudentOnTheLesson.objects.filter(lesson=pk).values_list("student", flat=True))
		people = User.objects.filter(id__in=studento_ids)
		serializer = StudentListSerializer(people, many=True)
		return Response(serializer.data)

class GroupPairsView(APIView):
	def get(self, request, pk):
		group_lessons = Lesson.objects.filter(lesson_group=pk)
		serializer = LessonListSerializer(group_lessons, many=True)
		return Response(serializer.data)

class ReportView(APIView):
	def get(self, request, pk):
	    reports = StudentOnTheLesson.objects.filter(student=pk)
	    serializer = ReportListSerializer(reports, many=True)
	    return Response(serializer.data)
