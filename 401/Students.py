class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    
    def getMajor(self):
        return self.major
    
    def setMajor(self, major):
        self.major = major
        
    def setCourses(self, courses):
        self.courses = courses
        
    def getCourses(self):
        return self.courses

    def getCoursesDisplay(self):
        courses = self.courses
        for course in courses:
            print(course.getCourseTitle(), course.getCourseTime())