# programa para implementar los operadores aritmeticos

print("----------------------------------------------")
print("-------------INVERTIR NUMERO------------------")
print("----------------------------------------------")

# INPUT

n = int(input("DIGITE EL VALOR: "))

# processing
x =  n%10
y = n//10
p = y%10
q = n//100

ni = x*100 + p*10 + q

#output

print("----------------------------------------------")
print("---------------------RESULTADOS---------------")
print("----------------------------------------------")


print ("valor invertido: " + str(ni))


