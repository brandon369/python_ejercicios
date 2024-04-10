def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

def find_primes(numbers):
    for num in numbers:
        if is_prime(num):
            print("Prime number found:", num)
            break
    else:
        print("No prime numbers found")

# Ejemplo de uso
numbers = [4, 6, 7, 9, 10, 11, 13]
find_primes(numbers)
