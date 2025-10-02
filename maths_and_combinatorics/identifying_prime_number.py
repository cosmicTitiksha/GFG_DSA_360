# The program is to check if a number is prime or not
import math
# num = int(input("Enter the number you want to check: "))
# lista = []
# for i in range(2,num):
#   if num % i == 0:
#     lista.append(i)
# if len(lista) == 0:
#   print("The number is prime.")
# else:
#   print("The number is not prime.")

num = int(input("Enter the number : "))
lista = []
def prime(num):
  for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
      lista.append(i)
  return lista
if num <= 1:
  print("The number is not prime. Numbers less than or equal to 1 are not prime.")

else:
  prime(num)
  if len(lista) == 0:
    print("The number is prime.")
  else:
    print("The number is not prime.")