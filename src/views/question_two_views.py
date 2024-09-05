from colorama import init, Style, Fore
from src.controller.utils import clear_terminal
class QuestionTwoViews:
    init()

    @staticmethod
    def question_two_views():
        clear_terminal()
        try:
            number = int(input(f"{Fore.BLUE}Digite um número: {Style.RESET_ALL}"))
            return number
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Entrada inválida! Por favor, insira um número inteiro.{Style.RESET_ALL}")
            input(f"{Fore.BLUE} Pressione enter para continuar... {Style.RESET_ALL}")
            return QuestionTwoViews.question_two_views()