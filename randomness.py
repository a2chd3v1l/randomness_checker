n = int(input('No of trials you want to try :'))
y = int(input('No of times you want to make trails :'))
def headtail() :
  import random
  options  = ['H', 'T']
  matrix = []
  Heads = 0
  Tails = 0
  for i in range(n):
      v =  random.choice(options)
      if v=="H" :
         Heads += 1
      else :
         Tails +=1 
  print(f'Heads = {Heads}')
  print(f'Tails = {Tails}')

if __name__ == "__main__":
    i = 0 
    while i < y :
      headtail()
      i +=1
      print()