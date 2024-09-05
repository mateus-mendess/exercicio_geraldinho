from src.views.question_four_views import QuestionFourViews
from src.controller.question_four_controller import QuestionFourController

class QuestionFourConstructor:

    @staticmethod
    def question_four_constructor():
        number = QuestionFourViews.question_four_views()

        question_four_controller = QuestionFourController(number)
        question_four_controller.question_four()
