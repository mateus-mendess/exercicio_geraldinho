from colorama import init, Fore, Style
init()

#Classe da segunda questão
class QuestionTwoController:
    numero_inicial = 0 #Número inicial

    def __init__(self, number):
        self.number = number

    def question_two(self):
        if self.numero_inicial < self.number:
            self.numero_inicial += 1
            print(self.numero_inicial)
            self.question_two() #Função recursiva
        else:
            input(f"{Fore.BLUE}Pressione enter para continuar...{Style.RESET_ALL}")
