def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

# Test the function
start = 1
end = 20
print(f"Prime numbers between {start} and {end}:")
print_primes_in_range(start, end)
