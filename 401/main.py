from Students import Student
from Course import Course

name = input("Enter student name: ")
major = input("Enter student major: ")

thisGuy = Student(name,major)
print("Current Major: ", thisGuy.getMajor())

courses = []

while True:
    title = input("Course title: ")
    time = input("Course time: ")
    newCourse = Course(title, time)
    courses.append(newCourse)

    if (input("More? (Y / N) ") == 'N'):
        break

thisGuy.setCourses(courses)
thisGuy.getCoursesDisplay()