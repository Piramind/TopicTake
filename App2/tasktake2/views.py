from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson
from .serializers import LessonListSerializer


class LessonListView(APIView):

	def get(self, request):
		lessons = Lesson.objects.filter(draft=False)
		serializer = LessonListSerializer(lessons, many=true)
		return Response(serializer.data)

# Create your views here.
