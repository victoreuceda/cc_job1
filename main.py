import sys

def fibonacci(n):
  fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
  for i in range(2, n):
    fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
  return fib_sequence[:n]

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python fibonacci.py <n>")
    sys.exit(1)

  n = int(sys.argv[1])
  fib_numbers = fibonacci(n)
  for num in fib_numbers:
    print(num)
