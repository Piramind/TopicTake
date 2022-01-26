from django.contrib import admin
from .models import StudyGroup, User, Discipline, Topic, Lesson, StudentOnTheLesson


admin.site.register(StudyGroup)
admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('user_first_name', 'user_last_name', 'group_name')
    fieldsets = (
        (None, {
            'fields': ('','', 'id')
        }),
        ('', {
            'fields': ('', '')
        }),
    )
admin.site.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_filter = ('', '')

admin.site.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ('topic_name', 'topic_user', 'topic_group')
    
admin.site.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_filter = ('', '')
    
admin.site.register(StudentOnTheLesson)

# Register your models here.
