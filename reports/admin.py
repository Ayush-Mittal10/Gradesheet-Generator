from django.contrib import admin
from reports.models import *
from .views import *


admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(SubjectMarks, SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    ordering = ['student_rank']

    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        return subject_marks.aggregate(marks = Sum('marks'))['marks']

admin.site.register(ReportCard, ReportCardAdmin)