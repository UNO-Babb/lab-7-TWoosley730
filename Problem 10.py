#Problem10.py
#Project problem 10

from NumberTests import isPrime


def main():
  limit = 2000000
  def sum_of_primes(limit):
    for num in range(2, limit):
        if is_prime(num):
            total += num
    return total
    print(total)
  
  

if __name__ == '__main__':
  main()
