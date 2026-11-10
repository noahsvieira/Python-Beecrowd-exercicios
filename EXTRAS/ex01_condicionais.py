'''
Sua missão é criar um programa que ajude o porteiro de uma masmorra perigosa. 

O programa deve receber o nível de um jogador.

Se o nível for maior ou igual a 10, o programa deve escrever na tela: Liberado para a Batalha

Se o nível for menor que 10, o programa deve escrever: Treine mais

'''

nivel_jogador = int(input())

if nivel_jogador >= 10 :
    print("Liberado para a Batalha")
else:
    print("Treine mais")