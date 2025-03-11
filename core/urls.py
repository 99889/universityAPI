from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, CourseViewSet, StudentViewSet, ProfessorViewSet, EnrollmentViewSet, AssignmentViewSet, SubmissionViewSet, GradeViewSet, SemesterViewSet, ResearchPaperViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'courses', CourseViewSet)

router.register(r'students', StudentViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'enrollments', EnrollmentViewSet)

router.register(r'assignments', AssignmentViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'grades', GradeViewSet)

router.register(r'semesters', SemesterViewSet)
router.register(r'researchpapers', ResearchPaperViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]