#Love Calculator
print("Welcome to the love calculator")
name1=input("What is your name?\n")
name2=input("What is their name?\n")
name=name1+name2
name.lower()
t=name.count("t")
r=name.count("r")
u=name.count("u")
e=name.count("e")
l=name.count("l")
o=name.count("o")
v=name.count("v")
e=name.count("e")
a=t+r+u+e
b=l+o+v+e
total=int(str(a)+str(b))
if total >=90 or total<=10:
    print(f"Your score is {total}, you go together like coke and mentos")
elif total >=40 or total<=50:
    print(f"Your score is {total}, you are alright together")
else:
    print(f"Your score is {total}")