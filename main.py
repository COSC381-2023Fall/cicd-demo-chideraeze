from fastapi import FastAPI, HTTPException
from course import courses
from student import Student

app = FastAPI()

students = {}  # Add a dictionary to store students

@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # return all the courses under the prefix
    results = []
    for course in courses:
        if course.is_prefix(prefix):
            results.append(course)
    
    return results

@app.post("/register-course/{eid}")
def register_course(eid: str, course_prefix: str, course_number: str):
    # Check if the student exists
    if eid not in students:
        raise HTTPException(status_code=404, detail=f"Student with ID {eid} not found")

    student = students[eid]

    # Check if the course exists
    course_exists = any(course.is_prefix(course_prefix) for course in courses)
    if not course_exists:
        raise HTTPException(status_code=404, detail=f"Course {course_prefix} {course_number} not found")

    # Add the course to the student's registered courses
    student.registered_courses.append((course_prefix, course_number))

    return {"message": "Course registered successfully"}