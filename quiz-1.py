# programa para implementar los operadores aritmeticos
import math
print("----------------------------------------------")
print("-------------INVERTIR NUMERO------------------")
print("----------------------------------------------")

# INPUT

n = int(input("DIGITE EL VALOR: "))

# processing

mod = n//137
x =  n%10
y = n//10
p = y%10

ni = x*100 + p*10 + mod*1

#output

print("----------------------------------------------")
print("---------------------RESULTADOS---------------")
print("----------------------------------------------")


print ("valor invertido: " + str(ni))