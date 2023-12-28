import sys
def fibonacci(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    result = fibonacci(n - 1) + fibonacci(n - 2)
    print(result)
    return result

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python fibonacci.py <n>")
    sys.exit(1)

  n = int(sys.argv[1])
  for i in range(n):
    fibonacci(i)
