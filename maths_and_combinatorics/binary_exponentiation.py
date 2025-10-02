# The program is to find a**b mod m

def powMod(a, b, m):
  res = 1
  while b>=1:
    if b%2 == 1:
      res = (res*a)%m
      b -= 1
    else:
      a = (a*a)%m
      b //= 2
  return res


if __name__ == "__main__":
  a, b, m = map(int, input().split())
  print(powMod(a, b, m))