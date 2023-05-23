'''Objecdt are a collection of data (varaiables) & functions/methinds.

Classes are a code templatre for object creation
'''
#Errorinthe code
class Student:
    college_name="IIT Bombay"
    #attribute
    def __init__(self, name, age, dob): #Calling constructor
        print("Constructor has been called")
       self.name = name
       self.age = age
       self.dob = dob

    def print_name(self, name):
        print("Student name" + name)
        student_1 = Student("Tuba" , "20" , "28/10/2002")

        print(student_1.name, student_1.age, student_1.dob)


