#Exercício Python 11: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas

dis = float(input("Digite a distancia do veiculo em km/h: "))
if dis < 200:
    print("voce vai ser cobrado de R$", dis * 0.50)
else:
    print("voce vai ser cobrado de R$", dis * 0.45)
   
