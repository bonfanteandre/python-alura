import adivinhacao
import forca

print("*********************************")
print("******* Selecione um jogo *******")
print("*********************************")

print("1 - Adivinhação")
print("2 - Forca")

jogo = int(input("Digite o número do jogo: "))

if (jogo == 1):
    print("Abrindo jogo da adivinhação...")
    adivinhacao.jogar()
elif (jogo == 2):
    print("Abrindo jogo da forca...")
    forca.jogar()