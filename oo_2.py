# Create your classes here

class Student():
    """Stores student information"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question():
    """Stores question and the correct answer"""

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        """Asks question and returns if answer given matches correct answer"""
        
        given_answer = input(f"{self.question}> ")
        
        return given_answer == self.answer


class Exam():
    """List Questions"""

    questions = [] # not sure this should go here
    
    def __init__(self, exam_name):
        self.exam_name = exam_name


    def add_question(self, question_to_add):
        Exam.questions.append(question_to_add)


    def administer(self):
        """ Iterates through question list and counts correct answers """

        count = 0

        for question in Exam.questions:

            if question.ask_and_evaluate() == True:
                count += 1

        return count


class StudentExam():
    

    def __init__(self, student, exam, student_score):
        """Stores student information, exam type, and student score for that exam"""

        self.Student = student
        self.exam_name = exam
        self.student_score = student_score
        

    def take_test(self):
        """Administers exam and assigns score to StudentExam instance"""

        student_score = Exam.administer()
        print(f"{self.first_name} got a {student_score} on the exam") 

######################## ADDED FOR PT 4 ##########################################
class Quiz(Exam):
    """List Questions"""

    def administer():
        """ Iterates through question list and counts correct answers """

        count = 0
        total = 0

        for question in Exam.questions:

            total += 1

            if question.ask_and_evaluate() == True:
                count += 1

        if count / total >= 0.5:
            return 1
        
        else:
            return 0


class StudentQuiz(StudentExam):

    def take_test(self):
        """Administers exam and assigns score to StudentExam instance"""

        student_score = Quiz.administer()
        print(f"{self.first_name} got a {student_score} on the quiz") 

###################################################################################

def example():
   
    # Creates an exam:
    exam = Quiz("Midterm")

    # Defines a few questions for the exam:
    list_q = Question('Python lists are mutable, iterable, and what?','ordered')
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    pwd_q = Question('What does pwd stand for?','print working directory')

    # Adds a few questions to the exam:
    exam.add_question(set_q)
    exam.add_question(pwd_q)
    exam.add_question(list_q)

    # Creates a student:
    student_1 = Student("Karen", "Debugger", "0101 Computer Street")
    # student_2 = Student("Jacqui", "Console", "888 Binary Ave")


    # Administers the test for that student using the take_test method you wrote:
    score = StudentQuiz.take_test(student_1)

    # Instantiates a StudentExam, passing the student and exam you just created as arguments:
    student_and_exam = StudentQuiz(student_1, exam, score)
    
   
example()