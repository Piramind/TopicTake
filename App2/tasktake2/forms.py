from django import forms
from .models import StudentOnTheLesson


class ReportForm(forms.ModelForm):
    class Meta:
        model = StudentOnTheLesson
        fields = ['group', 'discipline', 'topic', 'lesson', 'student']
