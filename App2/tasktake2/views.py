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
	'''All lessons'''
	def get(self, request):
		lessons = Lesson.objects.all()
		serializer = LessonSerializer(lessons, many=True)
		return Response(serializer.data)

# Create your views here.
class StudentsIView(APIView):
	'''Students that give reports on the lesson'''
	def get(self, request, pk):
		studento_ids = list(StudentOnTheLesson.objects.filter(lesson=pk).values_list("student", flat=True))
		people = User.objects.filter(id__in=studento_ids)
		serializer = StudentSerializer(people, many=True)
		return Response(serializer.data)

class GroupPairsView(APIView):
	'''Lessons of pk group'''
	def get(self, request, pk):
		group_lessons = Lesson.objects.filter(lesson_group=pk)
		serializer = LessonSerializer(group_lessons, many=True)
		return Response(serializer.data)

class StudentGroupsView(APIView):
	'''All student groups'''
	def get(self, request):
		groups = StudyGroup.objects.all()
		serializer = StudentGroupSerializer(groups, many=True)
		return Response(serializer.data)

class ReportView(APIView):
	'''Reports of the student'''
	def get(self, request):
		reports = StudentOnTheLesson.objects.filter(student=request.user)
		serializer = ReportSerializer(reports, many=True)
		return Response(serializer.data)

class ReportCreateView(APIView):
	'''Reports of the student'''
	def post(self, request):
		report = request.data.get("StudentOnTheLesson")
		serializer = ReportSerializer(data=report)
		if serializer.is_valid(raise_exception=True):
			report_saved = serializer.save(student=request.user)
		return Response({"Success": "Report created successfuly"})

