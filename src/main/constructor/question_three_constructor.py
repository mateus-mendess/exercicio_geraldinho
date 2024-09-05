from src.views.question_three_views import QuestionThreeViews
from src.controller.question_three_controller import QuestionThreeController

class QuestionThreeConstructor:

    @staticmethod
    def question_three_constructor():
        number = QuestionThreeViews.question_three_views()

        question_three_controller = QuestionThreeController(number)
        question_three_controller.question_three()

    