CONSTANTE_BONUS = 1000

nome_user = input("Digite seu nome ")

print ("Seja muito bem vindo " + nome_user )

salario = float(input("Digite o valor do seu salario "))

bonus = float(input("Digite o valor do bonus recebido "))

valor_bonus = CONSTANTE_BONUS + salario * bonus

print (f"O usuario {nome_user} possui o salario de {salario} e bonus de {valor_bonus}")




