x = int(input("Enter number: "))

a,b = 0 ,1

print("Fibonbacci: ")

for i in range(x):
    print(a,end=" ")
    a,b= b,a+b

 