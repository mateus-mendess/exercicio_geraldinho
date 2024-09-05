from colorama import init, Fore, Style
init()

#Classe que guarda a primeira questão
class QuestionOneController:
    def __init__(self, number):
        self.number = number

    def question_one(self):
        if self.number > 0:
            print(self.number)
            self.number-= 1
            self.question_one() #Utilizando a função recursiva
        else:
            input(f"{Fore.BLUE}Pressione enter para continuar...{Style.RESET_ALL}")

    