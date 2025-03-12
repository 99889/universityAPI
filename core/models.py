from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    established_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        from datetime import date
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        if age < 18:
            raise ValidationError(_("Student must be at least 18 years old."))

class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='professors')
    courses = models.ManyToManyField(Course, related_name='professors', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='assignments')

    def __str__(self):
        return self.title

class Submission(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.student} submitted {self.assignment}"

class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"

class Semester(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    courses = models.ManyToManyField(Course, related_name='semesters', blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError(_("Start date must be before the end date."))

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    publication_date = models.DateField()
    authors = models.ManyToManyField(Professor, related_name='research_papers')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='research_papers')

    def __str__(self):
        return self.title

    def clean(self):
        
        from datetime import date
        if self.publication_date > date.today():
            raise ValidationError(_("Publication date cannot be in the future."))