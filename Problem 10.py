#Problem10.py
#Project problem 10

from NumberTests import isEven
from NumberTests import fibonacciSequence

def main():
  nums = fibonacciSequence(4000001)
  print (nums)
  total = 0
  for fib in nums:
    if isEven(fib):
      total = total + fib
  
  print(total) # final answer

if __name__ == '__main__':
  main()
