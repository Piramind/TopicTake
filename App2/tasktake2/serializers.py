from rest_framework import serializers

from .models import *

class LessonListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = "__all__"


class LessonStudentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"
