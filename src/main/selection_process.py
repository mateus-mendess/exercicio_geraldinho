from src.main.constructor.screen_questions_constructor import ScreenQuestionsConstructor
from src.main.constructor.question_one_constructor import QuestionOneConstructor
from src.main.constructor.question_two_constructor import QuestionTwoConstructor
from src.main.constructor.question_three_constructor import QuestionThreeConstructor
from src.main.constructor.question_four_constructor import QuestionFourConstructor
from colorama import init, Style, Fore


class SelectionProcess:
    init()

    @staticmethod
    def selection_process():
        while True:
            option = ScreenQuestionsConstructor.screen_questions_constructor()
            match option:
                case 1:
                    QuestionOneConstructor.question_one_constructor()
                case 2:
                    QuestionTwoConstructor.question_two_constructor()
                case 3:
                    QuestionThreeConstructor.question_three_constructor()
                case 4:
                    QuestionFourConstructor.question_four_constructor()    
                case 5:
                    break
                case _:
                    print(f"{Fore.LIGHTRED_EX}Opção inválida!{Style.RESET_ALL}")
                    continue