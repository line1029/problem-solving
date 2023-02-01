n = int(input())
i = 2
limit = int(n**(0.5))+1
while i <= limit:
    while not n%i:
        print(i)
        n //= i
    limit = int(n**(0.5))+1
    i += 1
if n != 1:
    print(n)