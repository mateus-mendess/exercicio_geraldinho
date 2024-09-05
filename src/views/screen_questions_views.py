from colorama import init, Style, Fore
from src.controller.utils import clear_terminal
#Classe que suporta a tela principal do software
class ScreenQuestion:
    init() #Iniciando a mudança de cor nas strings

    @staticmethod
    def question_options():
        while True:
            clear_terminal() #Responsável por limpar o termoinal anterior
            print(f"""{Fore.BLUE}---@ Exercicio Geraldinho @---{Style.RESET_ALL}
[{Fore.BLUE}1{Style.RESET_ALL}] Questão 1
[{Fore.BLUE}2{Style.RESET_ALL}] Questão 2
[{Fore.BLUE}3{Style.RESET_ALL}] Questão 3
[{Fore.BLUE}4{Style.RESET_ALL}] Questão 4
[{Fore.BLUE}5{Style.RESET_ALL}] Sair """)
            opcao = int(input(f"{Fore.BLUE}Insira a opção desejada: {Style.RESET_ALL}")) #Escolha
            return opcao
