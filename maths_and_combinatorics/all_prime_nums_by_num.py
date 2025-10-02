############################################
# METHOD 3 - Sieve of Eratosthenes
############################################

def sieve(num):

  # create a boolean list to track prime states of numbers
  prime = [True] * (num + 1)
  p = 2

  # Sieve of Eratosthenes algorithm
  while p*p <= num :
    if prime[p]:
      # Mark all multiples of p as non-prime
      for i in range(p*p, num+1, p):
        prime[i] = False
    p+=1

  # Collect all prime numbers
  res = []
  for p in range(2, num+1):
    if prime[p]:
      res.append(p)

  return res



if __name__ == "__main__":
  num = int(input("Enter the number : "))
  res = sieve(num)
  for element in res:
    print(element , end = ' ')