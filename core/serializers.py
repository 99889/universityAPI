from rest_framework import serializers
from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['url', 'id', 'name', 'code', 'established_date', 'budget', 'description']
    def validate_budget(self, value):
        if value < 0:
            raise serializers.ValidationError("Budget must be a positive value.")
        return value

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['url', 'id', 'name', 'code', 'credits', 'department', 'prerequisites']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'id', 'first_name', 'last_name', 'date_of_birth', 'email', 'department', 'courses']
    def validate(self, data):
        date_of_birth = data.get('date_of_birth')
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        if age < 18:
            raise serializers.ValidationError("Student must be at least 18 years old.")
        return data

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields = ['url', 'id', 'first_name', 'last_name', 'date_of_birth', 'email', 'department', 'courses']
    
    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must end with @example.com")
        return value

class EnrollmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['url', 'id', 'student', 'course', 'enrollment_date', 'grade']
    def validate_grade(self, value):
        
        valid_grades = ['A', 'B', 'C', 'D', 'F']
        if value not in valid_grades:
            raise serializers.ValidationError(f"Grade must be one of {valid_grades}.")
        return value

class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assignment
        fields = ['url', 'id', 'title', 'description', 'due_date', 'course', 'professor']
    def validate_due_date(self, value):
        
        from datetime import date
        if value < date.today():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submission
        fields = ['url', 'id', 'assignment', 'student', 'submission_date', 'file', 'grade']

    def validate_file(self, value):
        
        max_size = 5 * 1024 * 1024  
        if value.size > max_size:
            raise serializers.ValidationError("File size must not exceed 5MB.")
        return value

class GradeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grade
        fields = ['url', 'id', 'student', 'course', 'grade', 'semester']

class SemesterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Semester
        fields = ['url', 'id', 'name', 'start_date', 'end_date', 'courses']

    def validate(self, data):
        
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("Start date must be before the end date.")
        return data


from datetime import date
class ResearchPaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ResearchPaper
        fields = ['url', 'id', 'title', 'abstract', 'publication_date', 'authors', 'department']

        def validate_publication_date(self, value):
        
        
            if value > date.today():
                raise serializers.ValidationError("Publication date cannot be in the future.")
            return value