function generateFibonacci(n) {
  let fibonacci = [0, 1];

  for (let i = 2; i < n; i++) {
    fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
  }

  return fibonacci;
}

function printFibonacci(n) {
  const fibonacci = generateFibonacci(n);

  for (let i = 0; i < n; i++) {
    console.log(fibonacci[i]);
  }
}

const n = process.argv[2] || 10;
printFibonacci(n);
