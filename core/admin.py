
from django.contrib import admin
from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

# Register your models here
admin.site.register(Department)
admin.site.register(Course)


admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Enrollment)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(Grade)
admin.site.register(Semester)
admin.site.register(ResearchPaper)
