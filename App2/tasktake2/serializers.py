from rest_framework import serializers

from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson

class LessonListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ["id", "lesson_date", "lesson_group", "lesson_disciple", "lesson_students", "lesson_topics"]