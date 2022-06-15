from django.contrib import admin
from .models import Feedback, Choice, Question
# Register your models here.
admin.site.register(Feedback)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_content']}),
    ('Date Information', {'fields':[], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]


#admin.site.register(Choice)
#admin.site.register(Question)
admin.site.register(Question, QuestionAdmin)
