def is_prime(num):
  for i in range(2, num):
    if num % i == 0:
      return False
   return True

for i in range(1000):
  if "3" in i:
    if "33" in i:
      if is_prime(i):
        print(f"*i&")
      else:
        print(f"*i")
    else:
      if is_prime(i):
        print(f"*i")
      else:
        print(f"i")
   else:
     print("i")
      
