init =print("Type the value: \n")
val = (input(init))
'''
typecheck = type(val)
print(typecheck)
if type(typecheck) is str:
    print("WTF?!")
'''
val = int(val)

if (val %2 == 0)and(val>0):
     print("This number is divisible by 2\t")
     print("& is a positive number\t")
elif(val %2 == 0)and(val<0):
     print("This number is divisible by 2\t")
     print("& is a negative number\t")
elif(val %2 == 1)and(val>0):
     print("This number is not divisible by 2\t")
     print("& is a positive number\t")
elif(val %2 == 1)and(val<0):
     print("This number is not divisible by 2\t")
     print("& is a negative number\t")
elif(val==0):
     print("This number is zero\t")

