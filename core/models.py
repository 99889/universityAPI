
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    established_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    prerequisites = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Professor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    enrollment_date = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='submissions/')
    grade = models.CharField(max_length=2, blank=True, null=True)



    def __str__(self):
        return f"{self.student} submitted {self.assignment}"



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    grade = models.CharField(max_length=2)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"

class Semester(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    
    end_date = models.DateField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    publication_date = models.DateField()
    authors = models.ManyToManyField(Professor)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title