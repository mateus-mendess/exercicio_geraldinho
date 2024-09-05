#Importando a função que colore strings
from colorama import Fore, Style, init
init() #Inicializando a função colorama

class QuestionFourController:
    sequence = [0, 1] #Lista para guardar os valores da sequencia de fibonacci

    def __init__(self, number):
        self.number = number + 1 #Pedindo o valor exato, pós as listas começam com indice 0
        self.number_view = number

    #Função que cria a sequencia
    def question_four(self):
        if len(self.sequence) < self.number:
            new_value = self.sequence[-1] + self.sequence[-2]
            self.sequence.append(new_value)
            self.question_four() #Função recursiva
        else:
            self.value_view()
            input(f"{Fore.BLUE}Pressione enter para continuar...{Style.RESET_ALL}")

    #Função que exibe apenas o valor pedido
    def value_view(self):
        for number in range(len(self.sequence)): #loop que percorre os indices que existe na lista
            if number == self.number_view:
                print(f"{Fore.BLUE}O valor na sequência de fibonacci: {Style.RESET_ALL} {self.sequence[number]}") 