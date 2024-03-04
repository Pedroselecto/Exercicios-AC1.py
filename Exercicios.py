# Exercício 1: equações de segundo grau

a = float(input('Informe o parâmetro "a" da equação: '))
b = float(input('Informe o parâmetro "b" da equação: '))
c = float(input('Informe o parâmetro "c" da equação: '))

x1 = (-b + (b**2 - 4*a*c)**(1/2)) / 2*a
x2 = (-b - (b**2 - 4*a*c)**(1/2)) / 2*a

print("A primeira raiz da equação é: ", x1)
print("A segunda raiz da equação é: ", x2)


# Exercício 2: anos bissextos

ano = int(input("Informe o ano: "))

print (bool(ano % 100 != 0 and ano % 4 == 0) or (ano % 100 == 0 and ano % 400 == 0))

