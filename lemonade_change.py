def lemonadechange(bills:list):
  fives,tens=0,0
  for i in bills:
    if i==5:
      fives+=1
    elif i==10:
      tens+=1
      if fives>=1:
        fives-=1
      else:
        return False
    else:
      if fives>=3:
        fives-=3
      elif fives>=1 and tens>=1:
        fives-=1
        tens-=1
      else:
        return False
  return True





print(lemonadechange([5,5,10,10]))