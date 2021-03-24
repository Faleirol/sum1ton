n = int(input("Enter a number"))
total = 0
# /n is in there at the end of a print statement
for i in range(n):
    print(i + 1)
    i = i +1
    total = total + i
print("The total is :" , total)
