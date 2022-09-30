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


    def administer():
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
        

    def take_test():
        """Administers exam and assigns score to StudentExam instance"""

        student_score = Exam.administer()
        print(f"Score: {student_score}") 



def example():
   
    # Creates an exam:
    exam = Exam("Midterm")

    # Defines a few questions for the exam:
    list_q = Question('Python lists are mutable, iterable, and what?','ordered')
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    pwd_q = Question('What does pwd stand for?','print working directory')

    # Adds a few questions to the exam:
    exam.add_question(set_q)
    exam.add_question(pwd_q)
    exam.add_question(list_q)


    # Creates a student:
    student_1 = Student("Jasmine", "Debugger", "0101 Computer Street")
    # student_2 = Student("Jacqui", "Console", "888 Binary Ave")


    # Administers the test for that student using the take_test method you wrote:
    score = StudentExam.take_test()

    # Instantiates a StudentExam, passing the student and exam you just created as arguments:
    student_and_exam = StudentExam(student_1, exam, score)

    
   
example()

    # Part 4:
   
"""
    When you call the administer method on a quiz, it should return 1 if you passed or 0 if you failed.
    Think about how you could solve this requirement: you have an Exam class and you want to have a Quiz class that is similar.

    As you saw in Part 4 with StudentExam, you will also need a new class, StudentQuiz, that allows a student to take a quiz and stores the score received.

    Write code to solve this problem. Incorporate as many of the “design” parts of the classes lectures as you feel comfortable with.
    """

### Removed Code:
    # From Exam def __init__
        # exams = {"midterm" : [], "final" : []}
        # midterm = []
        # final = []


        # alberta_capital = Question("What is the capital of Alberta?", "Edmonton", "Midterm")
        # python_author = Question("Who is the author of Python?", "Guido Van Rossum", "Midterm")
        # ubermelon_competitor = Question("", "", "Final")
        # balloonicorn_color = Question("", "", "Final")