def generate_primes(min, max):
    primes = []
    for num in range(min, max + 1):
        if isPrime(num):
            primes.append(num)
    return primes

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(generate_primes(0, 15))
                    
    
