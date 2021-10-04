'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if (n==0 or n==1):
    return False
  for d in range(2, n//2):
    if (n%d==0):
      return False
    return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  prod = 1
  for el in range(0, len(lst)):
   prod = prod * lst[el]
  return prod
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x!=y:
    if x>y:
      x=x-y
    else:
      y= y-x
  return x

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  while y!=0:
    z=x%b
    x=y
    y=z
  return x
  
  
def main():
  # interfata de tip consola aici
  print ('''
1.IS prime
2.Product
3.Cmmdc v1
3.Cmmdc v2
''')
  a=int(input("Comanda:"))
  if (a==1):
    # is prime
    n=int(input("Introduceti n="))
    print(is_prime(n))
  if (a==2):
    # product
    n=int(input("Introduceti n="))
    list = []
    for i in range(0,n):
      el=int(input())
      list.append(el)
    # print(list)
    # print(len(list)) #lungimea
    print(get_product(list))
  if (a==3):
    # is cmmdc 1
    x=int(input("Int x="))
    y=int(input("Int y="))
    print(get_cmmdc_vl(x, y))
  if (a==4):
    # is cmmdc 2
    x=int(input("Int x="))
    y=int(input("Int y="))
    print(get_cmmdc_v2(x, y))
    

if __name__ == '__main__':
  main()

  
