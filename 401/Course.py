class Course:
    def __init__(self, title, time):
        self.title = title
        self.time = time
    
    def getCourseTitle(self):
        return self.title
    
    def setCourseTitle(self, title):
        self.title = title
        
    def getCourseTime(self):
        return self.time
    
    def setCourseTime(self, time):
        self.time = time