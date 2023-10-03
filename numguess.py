#this is a program to guess a number using python, it also gives the no. of tries and % of you being correct
import random
num=random.randint(0,9)
#redo:
x=int(input("Enter your guess: "))
#def gus():
t=1
print(num)
while(x!=num):
 if(x==num):
   print(x, "is not the correct guess")
   t+=1
 elif (x<num):
   print(x,"is much lesser")
   x=int(input("Enter your guess: "))
   t += 1
 else:
   print(x,"is much greater")
   x=int(input("Enter your guess: "))
   t += 1
print(f"It took you {t} tries to find the number {num}")
tp=float(100/t)
print(f"You were right {tp}% of the time!")
#vijaysharanv
