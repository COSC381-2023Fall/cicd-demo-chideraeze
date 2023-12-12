# test_student.py
from student import Student
import pytest

@pytest.fixture
def student():
    return Student("E123", "John Doe")

def test_register_course(student):
    student.register_course("COSC", "111")
    assert student.registered_courses == ["COSC111"]

def test_get_registered_courses(student):
    student.register_course("COSC", "111")
    student.register_course("MATH", "101")

    registered_courses = student.get_registered_courses()
    assert registered_courses == ["COSC111", "MATH101"]

def test_register_course_invalid(student):
    with pytest.raises(ValueError, match="Invalid course prefix or number"):
        student.register_course("INVALID", "999")
