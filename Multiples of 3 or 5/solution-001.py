# Question :
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

N = 1000 # The number below which we want to find the sum of multiples of 3 or 5
# We have to find below N, so we will use N-1 in the formula
N = N-1
# We will use the formula for sum of arithmetic progression

# sum = n/2 * (2*a + (n-1)*d)
# Where a is the first term,
#       d is the common difference,
#       n is the number of terms.

# Number of terms in the series multiple of 3
three_n = N//3

# Number of terms in the series multiple of 5
five_n = N//5

# Number of terms in the series multiple of 15
fivteen_n = N//15

# because we have to find the sum of multiples of 3 or 5, we have to remove the multiples of 15
# this makes sur to not count the same number twice as it is a multiple of both 3 and 5

# Sum of multiples of 3
sum_three = three_n/2 * (2*3 + (three_n-1)*3)

# Sum of multiples of 5
sum_five = five_n/2 * (2*5 + (five_n-1)*5)

# Sum of multiples of 15
fivteen_n = fivteen_n/2 * (2*15 + (fivteen_n-1)*15)

# Sum of multiples of 3 or 5 = Sum of multiples of 3 + Sum of multiples of 5 - Sum of multiples of 15

Ans = sum_three + sum_five - fivteen_n

print(int(Ans))
# Answer : 233168
