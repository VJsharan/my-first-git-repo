import  string
import  random
choice=input("Enter  your  choice  (odd/even):  ")
a=int(input("  enter  a  random  number  between  1-6:  "))
b=random.randint(1,6)
S=a+b
if(S%2==0 and  choice=="even"):
  x=input("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??:    ")
elif(S%2!=0 and  choice=="odd"):
  x=input("congrats  you  won  the  toss  \n  what  are  you  choosing  (batting/bowling)??:    ")
else:
  print("you  lost  the  toss")
  cric=["batting","bowling"]
  soos=random.choice(cric)
  print(f"The  computer  has  chose  to  {soos}")
  SUM=0
  
print(f"You chose {x}")
for  i  in  range(0,11,1):
  j=int(input("enter  run:  "))
  c=random.randint(1,6)
  print(f"computer  put{c}")
  if(j==c  and  i==0):
    print("golden  duck")
    break
  elif(j==c):
    SUM+=j
    print("you got out :(")
    print(f"You scored {SUM} runs")
    break
  else:
    SUM+=j
  

 
  
  
