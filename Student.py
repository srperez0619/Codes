#The student class that has set methods, a print method, and name, studentID, and numCourses attributes
class Student: 
    #create the three attributes for this class
    name = ""
    studentID = ""
    numCourses = 0

    #Default Constructor
    def __init__(self, inName, inStudentID, inNumCourses):
        self.name = inName
        self.studentID = inStudentID
        self.numCourses = inNumCourses

    #Function to set name
    def set_name(self, inName):
        self.name = inName

    #Function to set student id
    def set_studentID(self, inStudentID): 
        self.studentID = inStudentID

    #Function to set the number of courses
    def set_numCourses(self, inNumCourses): 
        self.numCourses = inNumCourses

    #Function to print the student instance
    def printStudent(self): 
        print("\nStudent Name: " + self.name)
        print("\nStudentID: " + self.studentID)
        print("\nNumber of Courses Taken: " + str(self.numCourses))
        print("\n")
        
#main method that creates three student instances
student1 = Student("Sam", "000988153", 4)
student2 = Student("Jason", "000123456", 5)
student3 = Student("Nic", "000112233", 3)

#Call to method to print the student instances
print("Initial information for the students")
student1.printStudent()
student2.printStudent()
student3.printStudent()

#Call to method to change the student id, number of courses, and name
student1.set_name("Samantha")
student2.set_studentID("000234678")
student3.set_numCourses(5)

#Call to method to print the student instances after changes
print("Saved changes to the student information")
student1.printStudent()
student2.printStudent()
student3.printStudent()