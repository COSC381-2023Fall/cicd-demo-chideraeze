# student.py

class Student:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name
        self.registered_courses = []

    def register_course(self, course_prefix, course_number):
        if not self.is_valid_course(course_prefix, course_number):
            raise ValueError("Invalid course prefix or number")

        course_id = f"{course_prefix}{course_number}"
        self.registered_courses.append(course_id)

    def get_registered_courses(self):
        return self.registered_courses

    def is_valid_course(self, course_prefix, course_number):
        valid_courses = ["COSC111", "MATH101", "ENG102"]
        return f"{course_prefix}{course_number}" in valid_courses
