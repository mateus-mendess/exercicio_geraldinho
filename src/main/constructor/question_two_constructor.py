from src.views.question_two_views import QuestionTwoViews
from src.controller.question_two_controller import QuestionTwoController

class QuestionTwoConstructor:

    @staticmethod
    def question_two_constructor():
        number = QuestionTwoViews.question_two_views()

        question_two_controller = QuestionTwoController(number)
        question_two_controller.question_two()