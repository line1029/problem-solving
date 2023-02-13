n = int(input())

# find k such that k*(k+1)//2 <= n < (k+1)*(k+2)//2
# k^2 + k - 2n = 0
# k = (-1 + sqrt(1 + 8n))/2
from math import sqrt
print(int((-1 + sqrt(1 + 8*n))/2))