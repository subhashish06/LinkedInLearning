
def find_prime_factors(n: int):
    """
    Finds all the prime factors of a given integer.
    Returns a list of prime factors, or an error message for invalid inputs.
    """
    factors = set()
    
    # Handle non-positive integers
    if n < 1:
        return "Enter only positive integers"
    
    # 1 is a special case
    if n == 1:
        return {1}
    
    # Extract all factors of 2 first, allowing us to skip even numbers later
    while n % 2 == 0:
        factors.add(2)
        n = int(n // 2)
    
    # Check for odd prime factors up to the square root of n
    i: int = 3
    while i * i <= n:
        # While i perfectly divides n, record it and reduce n
        while n % i == 0:  # type: ignore
            factors.add(i)
            n = n // i  # type: ignore
        # Move to the next odd number
        i += 2

    # If any remainder of n is left and is > 1, it must be prime itself
    if n > 1:
        factors.add(n)
        return factors
    
    return factors


if __name__ == '__main__':
    num = int(input("Enter the number you want to find prime factors for: "))
    print(f"The prime factors of {num} are: {find_prime_factors(num)}")
