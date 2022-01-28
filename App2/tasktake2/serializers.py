from rest_framework import serializers

from .models import *

class LessonListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


class ReportListSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentOnTheLesson
		fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentOnTheLesson
		fields = "__all__"
