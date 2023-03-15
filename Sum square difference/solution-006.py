N = 100

# the sum of the squares of the first N natural numbers
sum_squres = N*(N+1)*(2*N+1)/6

# the square of the sum of the first N natural numbers
squre_sum = (N*(N+1)/2)**2

# difference between the sum of the squares of the first N natural numbers and the square of the sum
Ans = squre_sum - sum_squres

print(int(Ans))
# 25164150