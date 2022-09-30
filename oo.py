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
        count = 0

        for question in Exam.questions:

            if question.ask_and_evaluate() == True:
                count += 1

        return count


class StudentExam():

    def __init__():
        """Initializes everything"""

    def take_test():
        """Administers exam and assigns score to StudentExam instance"""
        # print score


def example():
    """
    Creates an exam

    Adds a few questions to the exam

    These should be part of the function; no need to prompt the user for questions.

    Creates a student

    Instantiates a StudentExam, passing the student and exam you just created as arguments

    Administers the test for that student using the take_test method you wrote
    """

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