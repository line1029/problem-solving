# recursive sol
n = int(input())
def recursive(n):
    if n == 1:
        return ["*"]
    return ["*"*(4*n - 3),
            "*"+" "*(4*n - 5)+"*",
            *map(lambda x: "* "+x+" *", recursive(n-1)),
            "*"+" "*(4*n - 5)+"*",
            "*"*(4*n - 3)]
print(*recursive(n), sep="\n")