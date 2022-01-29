from rest_framework import serializers

from .models import *

class DisciplineSer(serializers.ModelSerializer):
	class Meta:
		model = Discipline
		fields = "__all__"

class TopicSer(serializers.ModelSerializer):
	class Meta:
		model = Topic
		fields = ["id", "topic_name"]

class StudyGroupSer(serializers.ModelSerializer):
	class Meta:
		model = StudyGroup
		fields = "__all__"

class StudentSer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ["id", "username"]

class LessonSer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ["id", "lesson_date"]


class LessonSerializer(serializers.ModelSerializer):
	lesson_discipline = DisciplineSer(read_only=True)
	lesson_group = StudyGroupSer(read_only=True)
	lesson_students = StudentSer(many=True, read_only=True)
	lesson_topics = TopicSer(many=True, read_only=True)
	class Meta:
		model = Lesson
		fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
	discipline = DisciplineSer(read_only=True)
	group = StudyGroupSer(read_only=True)
	student = StudentSer(read_only=True)
	topic = TopicSer(read_only=True)
	lesson = LessonSer(read_only=True)
	class Meta:
		model = StudentOnTheLesson
		fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
	user_group = StudyGroupSer(read_only=True)
	class Meta:
		model = User
		fields = "__all__"


class StudentGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = StudyGroup
		fields = "__all__"

