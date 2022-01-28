from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson
from .serializers import LessonListSerializer, StudentListSerializer, ReportListSerializer, ReportSerializer
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


@csrf_exempt
def pupils_list(request):
    """
    List all code students, or create a new report instance.
    """
    if request.method == 'GET':
        pupils = StudentOnTheLesson.objects.all()
        serializer = ReportSerializer(pupils, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
