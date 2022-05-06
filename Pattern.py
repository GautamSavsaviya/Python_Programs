# pattern printing
print("Enter a number of line for printing the pattern: ", end="")
num1 = int(input())
print("Enter 1 for UpWard pyramid or 0 for DownWard pyramid: ", end="")
bool1 = bool(int(input()))
print(bool1)

if bool1:  # if bool1 == True  (if not bool1) that mean bool1 == False
    for i in range(0, num1):
        for j in range(0, i + 1):
            print("* ", end="")
        print()
else:
    for i in range(num1, 0, -1):
        for j in range(0, i):
            print("* ", end="")
        print()
