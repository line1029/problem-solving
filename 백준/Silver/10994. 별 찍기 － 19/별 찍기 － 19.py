# iterative sol
n = int(input())
for i in range(n - 1):
    print("* "*i, "*"*(4*(n - i) - 3), " *"*i, sep="")
    print("* "*(i + 1), " "*(4*(n - i - 1) - 3), " *"*(i + 1), sep="")
print(" ".join(["*"]*(2*n - 1)))
for i in range(n - 2, -1, -1):
    print("* "*(i + 1), " "*(4*(n - i - 1) - 3), " *"*(i + 1), sep="")
    print("* "*i, "*"*(4*(n - i) - 3), " *"*i, sep="")