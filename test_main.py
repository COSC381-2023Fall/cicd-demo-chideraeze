from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from course import courses
from student import Student
import pytest

client = TestClient(app)

@pytest.fixture
def student():
    return Student("E123", "John Doe")

def test_get_courses(courseA):
    courses.append(courseA)

    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix": "COSC",
            "_course_number": "111",
            "_cap": 30,
            "_instructor": "John Doe",
            "_name": "Programming I",
            "_place": "PH 503",
            "_meeting_times": "TH 9:00"
        }]

    courses.pop()

def test_register_course(student, mocker):
    mocker.patch(
        'course.Course.is_prefix',
        return_value=True
    )

    mocker.patch(
        'main.students',
        {'E123': student}  # Mocking the students dictionary
    )

    response = client.post("/register-course/E123", json={"course_prefix": "COSC", "course_number": "111"})

    expected_response = {
        'detail': [
            {'input': None, 'loc': ['query', 'course_prefix'], 'msg': 'Field required', 'type': 'missing', 'url': 'https://errors.pydantic.dev/2.5/v/missing'},
            {'input': None, 'loc': ['query', 'course_number'], 'msg': 'Field required', 'type': 'missing', 'url': 'https://errors.pydantic.dev/2.5/v/missing'}
        ]
    }

    assert response.status_code == 422
    assert response.json() == expected_response
