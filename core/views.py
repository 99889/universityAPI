from rest_framework import viewsets, permissions

from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

from .serializers import DepartmentSerializer, CourseSerializer, StudentSerializer, ProfessorSerializer, EnrollmentSerializer, AssignmentSerializer, SubmissionSerializer, GradeSerializer, SemesterSerializer, ResearchPaperSerializer

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