def classify_number(n):
    factors = [i for i in range(1, n) if n % i == 0]
    sum_of_factors = sum(factors)
    
    if sum_of_factors == n:
        return "Perfect"
    elif sum_of_factors > n:
        return "Abundant"
    else:
        return "Deficient"

# Test the function
numbers = [6, 12]
for num in numbers:
    print(f"{num} is a {classify_number(num)} number")
