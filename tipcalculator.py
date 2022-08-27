# conta total
#percentual a dar
# quantas pessoas dividir a conta
# contar quanto cada um vai dar com 2 casa decimais

print("Bem vindo à calculadora de gorjeta.")
total_conta = float(input("Qual o valor total da conta?"))
porcentagem = float(input("Quantos % de gorjeta você quer dar?"))
total_pessoas = float(input("Em quantas pessoas vão dividir a conta?"))

total = (total_conta + total_conta * porcentagem/100) / total_pessoas
gorjeta = "{:.2f}".format(total) # para formatar ascasas decimais
print (f"Cada pessoa deve pagar: {gorjeta}")