function fibonacci(n) {
  if (n <= 1) {
    return n;
  }

  let fib = [0, 1];

  for (let i = 2; i <= n; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
  }

  console.log(fib[n]);
}

const n = parseInt(process.argv[2]);
fibonacci(n); // Change the argument to the desired Fibonacci number
