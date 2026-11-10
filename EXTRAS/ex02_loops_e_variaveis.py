'''
O Acumulador de Pontos (Loops e Variáveis)

Um herói completou 3 missões seguidas. 
Na primeira missão ele ganhou 50 pontos, 
na segunda ganhou 30 pontos e 
na terceira ganhou 20 pontos. 
Faça um programa que some todos esses pontos usando uma variável acumuladora e 
mostre o total final na tela.

'''
recompensas_missoes = [50 , 30 , 20]

pontos_totais = 0

for pontos in recompensas_missoes:
    pontos_totais = pontos_totais + pontos

print(f"Pontuação total do Herói :{pontos_totais}")
