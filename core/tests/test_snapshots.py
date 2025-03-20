import json  # Add this import
import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_department_list(snapshot):
    client = APIClient()
    url = reverse('department-list')
    response = client.get(url)
    assert response.status_code == 200
    
    snapshot.assert_match(json.dumps(response.json(), indent=2), 'department_list_snapshot')

@pytest.mark.django_db
def test_course_list(snapshot):
    client = APIClient()
    url = reverse('course-list')
    response = client.get(url)
    assert response.status_code == 200
    
    snapshot.assert_match(json.dumps(response.json(), indent=2), 'course_list_snapshot')

@pytest.mark.django_db
def test_student_list(snapshot):
    client = APIClient()
    url = reverse('student-list')
    response = client.get(url)
    assert response.status_code == 200
    
    snapshot.assert_match(json.dumps(response.json(), indent=2), 'student_list_snapshot')