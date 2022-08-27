import random

escolha = input("Escolha 0 para Pedra, 1 para Papel e 2 para tesoura.")

escolha_computador = random.randint(0,2)

rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if escolha == "0" and escolha_computador == 0:
    print ("EMPATE" + rock, rock)
elif escolha == "0" and escolha_computador == 1:
        print ("PERDEU, ESCOLHEU" + rock + "E O COMPUTADOR TIROU" + paper)
else: print ("GANHOU, ESCOLHEU" + rock + "E O COMPUTADOR TIROU" + scissors)

if escolha == "1" and escolha_computador == 0:
    print ("GANHOU")
elif escolha == "1" and escolha_computador == 1:
        print ("EMPATE")
else: print ("PERDEU")

