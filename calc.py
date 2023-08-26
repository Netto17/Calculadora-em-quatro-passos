print("--------------CALCULADORA--------------")
n1=float(input("Digite um número: "))
n2=float(input("Digite outro número: "))
soma=n1+n2
print("A soma dos valores é: ",soma)
subtracao=n1-n2
print("A diferença entre os valores é: ",subtracao)
mult=n1*n2
print("A multiplicação dos valores é: ",mult)
if n2!=0:
    div=n1/n2
    print("A divisão dos valores é: ",div)
else:
    print("Impissível dividir por 0!")
    