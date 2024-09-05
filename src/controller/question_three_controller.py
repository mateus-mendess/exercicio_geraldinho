from colorama import init, Fore, Style
init()

#Classe da Questão 3
class QuestionThreeController:
    number_two = 0

    def __init__(self, number):
        self.number = number
    
    def question_three(self):
        if self.number_two < self.number:
            self.number_two += 1
            value = self.number_two % 2
            if value != 0:
                print(self.number_two)
            self.question_three() #Chamando a função recursiva
        else:
            input(f"{Fore.BLUE}Pressione enter para continuar...{Style.RESET_ALL}")