from rest_framework import viewsets, permissions

from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

from .serializers import DepartmentSerializer, CourseSerializer, StudentSerializer, ProfessorSerializer, EnrollmentSerializer, AssignmentSerializer, SubmissionSerializer, GradeSerializer, SemesterSerializer, ResearchPaperSerializer
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Grade


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def annual_marksheet(self, request, pk=None):
        cache_key = f'student_{pk}_annual_marksheet'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        student = self.get_object()
        grades = Grade.objects.filter(student=student)
        serializer = GradeSerializer(grades, many=True)
        data = serializer.data
        cache.set(cache_key, data, timeout=60*60)  
        return Response(data)
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EnrollmentViewSet(viewsets.ModelViewSet):


    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()

    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()


    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ResearchPaperViewSet(viewsets.ModelViewSet):
    queryset = ResearchPaper.objects.all()
    serializer_class = ResearchPaperSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]