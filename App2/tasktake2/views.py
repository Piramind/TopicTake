from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson
from .serializers import LessonListSerializer, LessonStudentListSerializer


class LessonListView(APIView):

	def get(self, request):
		lessons = Lesson.objects.filter(draft=False)
		serializer = LessonListSerializer(lessons, many=true)
		return Response(serializer.data)

# Create your views here.
class StudentsIView(APIView):
	def get(self, request, pk):
		studento_ids = list(StudentOnTheLesson.objects.filter(lesson=pk).values_list("student", flat=True))
		people = User.objects.filter(id__in=studento_ids)
		serializer = LessonStudentListSerializer(people, many=True)
		return Response(serializer.data)