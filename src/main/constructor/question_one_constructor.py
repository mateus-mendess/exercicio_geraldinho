from src.views.question_one_views import QuestionOneViews
from src.controller.question_one_controller import QuestionOneController

class QuestionOneConstructor:

    @staticmethod
    def question_one_constructor():
        number = QuestionOneViews.question_one_views()
        
        question_one_controller = QuestionOneController(number)
        question_one_controller.question_one()
