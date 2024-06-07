import os 
from modulo import *

while True:
    print(f'{' '*20}𝐵𝐸𝑀-𝑉𝐼𝑁𝐷𝑂 𝐴𝑂 𝐴𝑃𝐿𝐼𝐶𝐴𝑇𝐼𝑉𝑂 𝐷𝑂 𝐵𝐴𝑁𝐶𝑂 𝐼𝑇𝐴𝑈́{' '*20}\n')
    exibir_menu()
    opcao = input('Você deseja?')
    match opcao:
        case '1':
             a = input('Informe o seu nome: ')
             print(cadastrar(a)) 