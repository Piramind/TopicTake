from rest_framework import serializers

from .models import *

class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudentOnTheLesson
		fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"


class StudentGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyGroup
		fields = "__all__"

