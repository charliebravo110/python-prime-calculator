#!/usr/bin/env python3
"""
# RELEASE NOTES
# Version: 1.5.0
# Date: 2025-06-09
# Changes:
# - Updated calculation from 25 to 30 prime numbers
# - Enhanced computational scope for more comprehensive results
# - Updated all documentation and comments to reflect new calculation range
# - Updated unit tests to validate 30 prime numbers (30th prime is 113)
# - Maintained all existing security features and optimizations

# Version: 1.4.0
# Date: 2025-09-05
# Changes:
# - Added comprehensive security vulnerability assessment
# - Implemented input validation limits to prevent DoS attacks
# - Added maximum value constraint (n <= 10000) for resource protection
# - Enhanced security comments and documentation
# - Maintained all existing functionality and optimizations

# Version: 1.3.0
# Date: 2025-09-05
# Changes:
# - Translated all user-facing literals from Spanish to French
# - Updated output messages and error handling to French language
# - Maintained all existing functionality and optimizations
# - Enhanced internationalization support

# Version: 1.2.0
# Date: 2025-09-05
# Changes:
# - Updated calculation from 50 to 100 prime numbers
# - Enhanced computational scope for more comprehensive results
# - Maintained all existing optimizations and error handling
# - Updated documentation to reflect new calculation range

# Version: 1.1.0
# Date: 2025-09-05
# Changes:
# - Enhanced code documentation and comments
# - Improved algorithm efficiency with optimized prime checking
# - Added comprehensive docstrings for all functions
# - Better formatted output display
# - Maintained calculation of first 50 prime numbers

Prime Number Calculator
Calculates and displays the first 30 prime numbers using an optimized algorithm.
This implementation uses trial division with optimizations for even numbers
and only checks odd divisors up to the square root of the candidate number.
"""

def is_prime(n):
    """
    Check if a number is prime using optimized trial division.
    
    This function implements an efficient primality test by:
    1. Handling edge cases (n < 2, n == 2)
    2. Quickly eliminating even numbers (except 2)
    3. Testing only odd divisors up to sqrt(n)
    
    Args:
        n (int): Number to check for primality
        
    Returns:
        bool: True if the number is prime, False otherwise
        
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)
    """
    # Numbers less than 2 are not prime by definition
    if n < 2:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n) for efficiency
    # Only need to check up to sqrt(n) because if n has a divisor > sqrt(n),
    # it must also have a corresponding divisor < sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def get_first_n_primes(n):
    """
    Generate the first n prime numbers using sequential candidate testing.
    
    This function systematically tests each number starting from 2
    until it finds the requested number of primes. It uses the is_prime()
    function to test each candidate for primality.
    
    Args:
        n (int): Number of primes to generate (must be positive)
        
    Returns:
        list: List containing the first n prime numbers in ascending order
        
    Raises:
        ValueError: If n is not a positive integer
        
    Time Complexity: O(n * sqrt(p_n)) where p_n is the nth prime
    Space Complexity: O(n) for storing the result list
    """
    # Security: Input validation to prevent integer overflow and resource exhaustion
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n doit être un entier positif")
    
    # Security: Limit maximum value to prevent excessive memory usage and DoS attacks
    if n > 10000:
        raise ValueError("n ne peut pas dépasser 10000 pour des raisons de sécurité")
    
    primes = []
    candidate = 2  # Start with the first prime number
    
    # Continue until we have found n prime numbers
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    
    return primes

def main():
    """
    Main function to calculate and display the first 30 prime numbers.
    
    This function orchestrates the prime calculation process and provides
    a user-friendly formatted output showing the results in a tabular format
    with 10 numbers per row for optimal readability.
    """
    # Display program header with clear indication of what's being calculated
    print("Calcul des 30 premiers nombres premiers...")
    print("=" * 50)
    
    try:
        # Calculate the first 30 prime numbers using our optimized algorithm
        primes = get_first_n_primes(30)
        
        # Display the results header
        print(f"Les {len(primes)} premiers nombres premiers sont :")
        print("-" * 50)
        
        # Print 10 numbers per line for better readability and organization
        # This creates a neat tabular display that's easy to scan
        for i in range(0, len(primes), 10):
            line = primes[i:i+10]  # Get the next batch of up to 10 numbers
            formatted_line = " ".join(f"{num:4d}" for num in line)  # Right-align with 4 digits
            print(f"{i+1:3d}-{min(i+10, len(primes)):3d}: {formatted_line}")
        
        # Display summary statistics
        print("-" * 50)
        print(f"Le plus grand nombre premier trouvé est : {primes[-1]}")
        print(f"Total des nombres premiers calculés : {len(primes)}")
        
    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()
