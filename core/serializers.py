from rest_framework import serializers
from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['url', 'id', 'name', 'code', 'established_date', 'budget', 'description']

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'id', 'name', 'code', 'credits', 'department', 'prerequisites']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'id', 'first_name', 'last_name', 'date_of_birth', 'email', 'department', 'courses']

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = ['url', 'id', 'first_name', 'last_name', 'date_of_birth', 'email', 'department', 'courses']

class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['url', 'id', 'student', 'course', 'enrollment_date', 'grade']

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ['url', 'id', 'title', 'description', 'due_date', 'course', 'professor']

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ['url', 'id', 'assignment', 'student', 'submission_date', 'file', 'grade']

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['url', 'id', 'student', 'course', 'grade', 'semester']

class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester
        fields = ['url', 'id', 'name', 'start_date', 'end_date', 'courses']

class ResearchPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = ['url', 'id', 'title', 'abstract', 'publication_date', 'authors', 'department']