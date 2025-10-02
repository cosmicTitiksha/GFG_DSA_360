# The program is to check if a number is prime or not

num = int(input("Enter the number you want to check: "))
lista = []
for i in range(2,num):
  if num % i == 0:
    lista.append(i)
if len(lista) == 0:
  print("The number is prime.")
else:
  print("The number is not prime.")