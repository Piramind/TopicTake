from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser


class StudyGroup(models.Model):
    group_name = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.group_name}"



class User(AbstractUser):
    user_last_name = models.CharField(max_length=20)
    user_first_name = models.CharField(max_length=20)
    user_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"


class Discipline(models.Model):
    discipline_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.discipline_name}"


class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    topic_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    topic_user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    def ____str____(self):
        return f"{self.topic_name}"


class Lesson(models.Model):                                                                 #вывести таблицу lesson
    lesson_date = models.DateTimeField(null=True)
    lesson_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    lesson_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    lesson_students = models.ManyToManyField(User, through="StudentOnTheLesson")
    lesson_topics = models.ManyToManyField(Topic, through="StudentOnTheLesson")


class StudentOnTheLesson(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
