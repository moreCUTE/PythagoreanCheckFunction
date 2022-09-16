def  PythagoreanCheck(a, b, c,):
    a= 0
    b= 0
    c= 0

    if (a**2 + b**2 == c**2): 
      return True
    else:
      return False

  
print("bive me first number")
a = int(input())
print("ur numerb is", a)
print("biuve me secong number")
b = int(input())
print("ur sencond numebr is", b)
print("give me third number")
c = int(input())
print("this is ur secong numner", c)



if  PythagoreanCheck(a, b, c):
  print("ye it works")
else:
  print("it dont wrok bruh")

PythagoreanCheck(a, b, c)
