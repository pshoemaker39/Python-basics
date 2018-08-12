from Students import Student
from Course import Course
import StudentDB

db = StudentDB.Student_DB()

def getStudentInfo():
    name = input("Enter student name: ")
    major = input("Enter student major: ")
    thisGuy = Student(name,major)
    print("Current Major: ", thisGuy.getMajor())
    db.addStudent(thisGuy)
    return thisGuy

while True:

    thisGuy = getStudentInfo()
    courses = []

    while True:
        title = input("Course title: ")
        time = input("Course time: ")
        newCourse = Course(title, time)
        courses.append(newCourse)

        if (input("More Courses? (Y / N) ").lower() == 'n'):
            break

    thisGuy.setCourses(courses)
    thisGuy.getCoursesDisplay()

    if (input("More Students? (Y / N) ").lower() == 'n'):
        break

print(db.getStudents())

thisName = input("Find a recently added student: ")
while True:
    db.findStudent(thisName)
    thisName = input("Find another recently added student: ")
    if thisName == '':
        break