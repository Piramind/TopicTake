from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson
from .serializers import LessonSerializer, StudentSerializer, ReportSerializer, ReportSerializer, StudentGroupSerializer
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView
from .forms import ReportForm




class LessonListView(APIView):

	def get(self, request):
		lessons = Lesson.objects.all()
		serializer = LessonSerializer(lessons, many=true)
		return Response(serializer.data)

# Create your views here.
class StudentsIView(APIView):
	def get(self, request, pk):
		studento_ids = list(StudentOnTheLesson.objects.filter(lesson=pk).values_list("student", flat=True))
		people = User.objects.filter(id__in=studento_ids)
		serializer = StudentSerializer(people, many=True)
		return Response(serializer.data)

class GroupPairsView(APIView):
	def get(self, request, pk):
		group_lessons = Lesson.objects.filter(lesson_group=pk)
		serializer = LessonSerializer(group_lessons, many=True)
		return Response(serializer.data)

class ReportView(APIView):
	def get(self, request):
		reports = StudentOnTheLesson.objects.filter(student=request.user)
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data)


@csrf_exempt
def pupils_list(request):
	"""
	List all code students, or create a new report instance.
	"""
	if request.method == 'GET':
		pupils = StudentOnTheLesson.objects.filter(student=request.user)
		serializer = ReportSerializer(pupils, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		serializer = ReportSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


class ReportViewSet(viewsets.ViewSet):
	"""
	A simple ViewSet for listing or retrieving users.
	"""
	queryset = StudentOnTheLesson.objects.all()

	def list(self, request):
		pupils = StudentOnTheLesson.objects.filter(student=request.user)
		serializer = ReportSerializer(pupils, many=True)
		return Response(serializer.data)

	def create(self, request):
		pass

class GroupViewSet(viewsets.ViewSet):
	"""
	A simple ViewSet for listing or retrieving users.
	"""
	queryset = StudyGroup.objects.all()

	def list(self, request):
		serializer = StudentGroupSerializer(self.queryset, many=True)
		return Response(serializer.data)

	@action(methods=['GET'], detail=True, url_path='list_pairs')
	def list_pairs(self, request):
		gg = self.get_object()
		group_lessons = Lesson.objects.filter(lesson_group=gg.id)
		serializer = LessonSerializer(group_lessons, many=True)
		return Response(serializer.data)

	@action(methods=['GET'], detail=True, url_path='list_students')
	def list_students(self, request):
		group_students = User.objects.filter(user_group=request.pk)
		serializer = StudentSerializer(group_students, many=True)
		return Response(serializer.data)


class AddReport(CreateView):
	model = StudentOnTheLesson
	form_class = ReportForm
	template_name = "create_sotl.html"

	def form_valid(self, form):
		form.instance.student  = self.request.user
		form.save()
		return redirect("/")

	def success_url(self):
		redirect("student/pupils_list/")
