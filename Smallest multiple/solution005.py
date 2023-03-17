# Question :
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Solution :

factors_ten = 2520
limit = 20 + 1 # for range settlement

# Finding Factors of 2520
def get_factors(num):
    # In factors array index represets the factor and the value of those index represents the 
    # occurence of these numbers
    factors = [0]*(limit)
    i = 2
    while num != 1:
        while num % i == 0:
            factors[i] += 1
            num //= i
        i += 1
    return factors

# combine two numbers factors (finding Factors of LCM of two numbers)
def combine(factors, num_factors):
    ans_factors = [0]*limit
    for i in range(limit):
        ans_factors[i] = max(factors[i], num_factors[i])
    return ans_factors

ans_factors = get_factors(2520)

for num in range(11, limit):
    ans_factors = combine(ans_factors, get_factors(num))

result = 1
for i in range(2,limit):
    result *= i**ans_factors[i]
    
print(result)
# Ans: 232792560