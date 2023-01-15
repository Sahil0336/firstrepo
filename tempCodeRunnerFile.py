def eval_series(n):
  if n == 1:
    return 2
  else:
    return 2*n + eval_series(n-1)
def main():
  n =int(input('Enter a number:-'))
  result = eval_series(n)
  print(f"The sum of the series 2+4+6+...+2n for n={n} is {result}")
main()
