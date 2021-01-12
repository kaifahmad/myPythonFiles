from LearnClassandObjects import Student
# Inside the Intern class we want to use all the functionality of Student Class
class Intern(Student) :
    def start_project(self):
        print("Starting Projects")

    def submit_assignment(self):
        print("Submitting Assignment")
