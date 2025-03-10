#Problem10.py
#Project problem 10

from NumberTests import isPrime
from NumberTests import fibonacciSequence

def main():
  def sum_of_primes(limit):
    """Return the summation of all prime numbers less than the given limit."""
    total = 0
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total
  
  

if __name__ == '__main__':
  main()
