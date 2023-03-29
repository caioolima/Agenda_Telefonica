agenda = {}

while True:

    menu = """\033[1;93m
     --- MENU ---
            
[1] INSERIR NOME E TELEFONE
[2] MUDAR NÚMERO
[3] REMOVER NOME
[4] SAIR

ESCOLHA: \033[m"""
  escolha = int(input(menu))

  if escolha == 1:
    nome1 = input("\nDigite o nome: ".upper())
    número1 = int(input("Número dele: ".upper()))

    if agenda.get(nome1):
      print(nome1,'já está cadastrado .'.upper())
    else:
      agenda[nome1] = número1
      print(agenda)
  elif escolha == 2:
    nome2 = input('\nNome para mudar o número: '.upper())
    um2 = int(input('Novo número: '.upper()))

    if nome2 in agenda.keys():
       agenda[nome2] = num2
    else:
       print('\nNão existe essa pessoa no sistema.'.upper())
       print(agenda)
   elif escolha == 3:
       nome3 = input('\nNome para tirar: '.upper())
       genda.pop(nome3)
       print('Nome retirado...'.upper())
    elif escolha == 4:
        print('Você decidiu sair...'.upper())
        exit()
    else:
        print('\nDigite um número válido.'.upper())
