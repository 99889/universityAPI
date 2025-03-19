from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Department, Course, Student, Professor, Enrollment, Assignment, Submission, Grade, Semester, ResearchPaper

class DepartmentTests(APITestCase):
    def test_create_department(self):
        url = reverse('department-list')
        data = {'name': 'Computer Science', 'code': 'CS', 'established_date': '2020-01-01', 'budget': '1000000.00', 'description': 'Department of Computer Science'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.count(), 1)
        self.assertEqual(Department.objects.get().name, 'Computer Science')

class CourseTests(APITestCase):
    def test_create_course(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        url = reverse('course-list')
        data = {'name': 'Introduction to Programming', 'code': 'CS101', 'credits': 3, 'department': department.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().name, 'Introduction to Programming')

class StudentTests(APITestCase):
    def test_create_student(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        url = reverse('student-list')
        data = {'first_name': 'John', 'last_name': 'Doe', 'date_of_birth': '2000-01-01', 'email': 'john.doe@example.com', 'department': department.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, 'John')

class ProfessorTests(APITestCase):
    def test_create_professor(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        url = reverse('professor-list')
        data = {'first_name': 'Jane', 'last_name': 'Smith', 'date_of_birth': '1975-05-15', 'email': 'jane.smith@example.com', 'department': department.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Professor.objects.count(), 1)
        self.assertEqual(Professor.objects.get().first_name, 'Jane')

class EnrollmentTests(APITestCase):
    def test_create_enrollment(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        student = Student.objects.create(first_name='John', last_name='Doe', date_of_birth='2000-01-01', email='john.doe@example.com', department=department)
        course = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3, department=department)
        url = reverse('enrollment-list')
        data = {'student': student.id, 'course': course.id, 'grade': 'A'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Enrollment.objects.count(), 1)
        self.assertEqual(Enrollment.objects.get().grade, 'A')

class AssignmentTests(APITestCase):
    def test_create_assignment(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        professor = Professor.objects.create(first_name='Jane', last_name='Smith', date_of_birth='1975-05-15', email='jane.smith@example.com', department=department)
        course = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3, department=department)
        url = reverse('assignment-list')
        data = {'title': 'Homework 1', 'description': 'Complete exercises 1-5', 'due_date': '2023-12-01', 'course': course.id, 'professor': professor.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Assignment.objects.count(), 1)
        self.assertEqual(Assignment.objects.get().title, 'Homework 1')

class SubmissionTests(APITestCase):
    def test_create_submission(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        student = Student.objects.create(first_name='John', last_name='Doe', date_of_birth='2000-01-01', email='john.doe@example.com', department=department)
        professor = Professor.objects.create(first_name='Jane', last_name='Smith', date_of_birth='1975-05-15', email='jane.smith@example.com', department=department)
        course = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3, department=department)
        assignment = Assignment.objects.create(title='Homework 1', description='Complete exercises 1-5', due_date='2023-12-01', course=course, professor=professor)
        url = reverse('submission-list')
        data = {'assignment': assignment.id, 'student': student.id, 'grade': 'A'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Submission.objects.count(), 1)
        self.assertEqual(Submission.objects.get().grade, 'A')

class GradeTests(APITestCase):
    def test_create_grade(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        student = Student.objects.create(first_name='John', last_name='Doe', date_of_birth='2000-01-01', email='john.doe@example.com', department=department)
        course = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3, department=department)
        url = reverse('grade-list')
        data = {'student': student.id, 'course': course.id, 'grade': 'A', 'semester': 'Fall 2023'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Grade.objects.count(), 1)
        self.assertEqual(Grade.objects.get().grade, 'A')

class SemesterTests(APITestCase):
    def test_create_semester(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        course = Course.objects.create(name='Introduction to Programming', code='CS101', credits=3, department=department)
        url = reverse('semester-list')
        data = {'name': 'Fall 2023', 'start_date': '2023-09-01', 'end_date': '2023-12-15', 'courses': [course.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Semester.objects.count(), 1)
        self.assertEqual(Semester.objects.get().name, 'Fall 2023')

class ResearchPaperTests(APITestCase):
    def test_create_research_paper(self):
        department = Department.objects.create(name='Computer Science', code='CS', established_date='2020-01-01', budget=1000000.00, description='CS Department')
        professor = Professor.objects.create(first_name='Jane', last_name='Smith', date_of_birth='1975-05-15', email='jane.smith@example.com', department=department)
        url = reverse('researchpaper-list')
        data = {'title': 'AI in Education', 'abstract': 'Exploring the impact of AI on education.', 'publication_date': '2023-01-01', 'authors': [professor.id], 'department': department.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ResearchPaper.objects.count(), 1)
        self.assertEqual(ResearchPaper.objects.get().title, 'AI in Education')