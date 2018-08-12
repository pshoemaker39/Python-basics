class Student_DB:
    def __init__(self):
        self.studDB = list()
    
    def addStudent(self, student):
        self.studDB.append(student)
        print("Student added successfully.")

    def getStudents(self):
        return self.studDB

    def findStudent(self, name):

        for student in self.studDB:
            if student.getName() == name:
                print("Found")