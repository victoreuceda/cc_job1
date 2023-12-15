#include <iostream>
#include <vector>

std::vector<int> fibonacci(int n)
{
  std::vector<int> sequence;
  int a = 0, b = 1;

  while (n--)
  {
    sequence.push_back(a);
    int next = a + b;
    a = b;
    b = next;
  }
  return sequence;
}

int main()
{
  int n = 20;

  std::vector<int> fib_sequence = fibonacci(n);
  std::cout << "Fibonacci sequence up to " << n << " terms:" << std::endl;
  for (int num : fib_sequence)
  {
    std::cout << num << " ";
  }
  std::cout << std::endl;

  return 0;
}
